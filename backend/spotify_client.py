import os
import requests
from google import genai
from dotenv import load_dotenv
import pycountry

load_dotenv()


class SpotifyClient:
    def __init__(self):
        self.client_id = os.getenv("SPOTIFY_CLIENT_ID")
        self.client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
        self.access_token = self.authenticate()


    def authenticate(self):
        auth_url = 'https://accounts.spotify.com/api/token'
        auth_response = requests.post(
            auth_url,
            data={'grant_type': 'client_credentials'},
            auth=(self.client_id, self.client_secret)
        )
        if auth_response.status_code != 200:
            raise Exception("Failed to authenticate with Spotify")
        return auth_response.json()['access_token']


    def get_headers(self):
        return {"Authorization": f"Bearer {self.access_token}"}
    

    def iso_to_country_name(self, country_iso):
        markets = ["AD", "AE", "AG", "AL", "AM", "AO", "AR", "AT", "AU", "AZ", "BA", "BB", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BN", "BO", "BR", "BS", "BT", "BW", "BY", "BZ", "CA", "CD", "CG", "CH", "CI", "CL", "CM", "CO", "CR", "CV", "CW", "CY", "CZ", "DE", "DJ", "DK", "DM", "DO", "DZ", "EC", "EE", "EG", "ES", "ET", "FI", "FJ", "FM", "FR", "GA", "GB", "GD", "GE", "GH", "GM", "GN", "GQ", "GR", "GT", "GW", "GY", "HK", "HN", "HR", "HT", "HU", "ID", "IE", "IL", "IN", "IQ", "IS", "IT", "JM", "JO", "JP", "KE", "KG", "KH", "KI", "KM", "KN", "KR", "KW", "KZ", "LA", "LB", "LC", "LI", "LK", "LR", "LS", "LT", "LU", "LV", "LY", "MA", "MC", "MD", "ME", "MG", "MH", "MK", "ML", "MN", "MO", "MR", "MT", "MU", "MV", "MW", "MX", "MY", "MZ", "NA", "NE", "NG", "NI", "NL", "NO", "NP", "NR", "NZ", "OM", "PA", "PE", "PG", "PH", "PK", "PL", "PR", "PS", "PT", "PW", "PY", "QA", "RO", "RS", "RW", "SA", "SB", "SC", "SE", "SG", "SI", "SK", "SL", "SM", "SN", "SR", "ST", "SV", "SZ", "TD", "TG", "TH", "TJ", "TL", "TN", "TO", "TR", "TT", "TV", "TW", "TZ", "UA", "UG", "US", "UY", "UZ", "VC", "VE", "VN", "VU", "WS", "XK", "ZA", "ZM", "ZW"]
        if country_iso in markets:
            country = pycountry.countries.get(alpha_2=country_iso)
            return country.name
        else:
            return None
        
    
    def get_country_code(self, lat, lon):
        url = 'https://api.opencagedata.com/geocode/v1/json'
        params = {
            'q': f'{lat},{lon}',
            'key': os.getenv('OPENCAGE_API_KEY'),
            'no_annotations': 1
        }
        response = requests.get(url, params=params)
        data = response.json()

        try:
            components = data['results'][0]['components']
            return components.get('country_code', None).upper()
        except (IndexError, AttributeError):
            return None
    

    def retrieve_request(self, country, playlists_string, playlist_names):
        gemini_prompt_question = f"Among the following comma-separated string of playlist names, give me ONLY the name of the single playlist from this list that will get me the current top 50 songs for {country}:\n\n"
        gemini_parameters_text_input = gemini_prompt_question + playlists_string + "\n\n"

        client = genai.Client(api_key=os.getenv("GEMINI_KEY"))
        response = client.models.generate_content(
            model="gemini-2.5-pro", contents=gemini_parameters_text_input
        )
        playlist_name = response.text

        while playlist_name not in playlist_names:
            client = genai.Client(api_key=os.getenv("GEMINI_KEY"))
            response = client.models.generate_content(
                model="gemini-2.5-pro", contents=gemini_parameters_text_input
            )
            playlist_name = response.text

        return playlist_name

        
    def get_playlist(self, country):
        url = f"https://api.spotify.com/v1/search"
        headers = {"Authorization": f"Bearer {self.access_token}"}
        params = {
            "q": f"Top 50 - {country}",
            "type": "playlist"
        }
        
        response = requests.get(url, headers=headers, params=params)
        playlists = response.json()["playlists"]["items"]

        playlist_names = []
        for playlist in playlists:
            if playlist != None:
                playlist_names.append(playlist["name"])
        playlists_string = ", ".join(playlist_names)

        playlist_name = self.retrieve_request(country, playlists_string, playlist_names)

        for playlist in playlists:
            if playlist != None:
                if playlist["name"] == playlist_name:
                    return playlist["id"]


    def get_top_fifty_songs(self, playlist_id):
        url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
        params = {
            'limit': 50,
            'market': 'US'
        }
        response = requests.get(url, headers=self.get_headers(), params=params)

        if response.status_code != 200:
            raise Exception(f"Failed to get top songs: {response.text}")
        data = response.json()
        top_tracks = []

        for item in data['items']:
            track = item['track']
            top_tracks.append({
                'name': track['name'],
                'artists': [artist['name'] for artist in track['artists']],
                'album': track['album']['name'],
                'image': track['album']['images'][0]['url'] if track['album']['images'] else None
            })

        return top_tracks
    

    def get_coordinates_to_songs(self, lat, lon):
        country_iso = self.get_country_code(lat, lon)
        country = self.iso_to_country_name(country_iso)
        playlist_id = self.get_playlist(country)
        return self.get_top_fifty_songs(playlist_id)