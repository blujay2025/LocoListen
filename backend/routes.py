from flask import current_app as app
from flask import request
from .database.database import Database
from .spotify_client import SpotifyClient
from psycopg.types.json import Json
from datetime import datetime, timedelta, timezone
import json


db = Database()
spotify_client = SpotifyClient()


@app.route('/get-top-tracks', methods=["POST", "GET"])
def get_top_tracks():
    lat = request.args.get('latitude')
    lon = request.args.get('longitude')

    country_code = spotify_client.get_country_code(lat, lon)
    if country_code == None:
        return json.dumps({
            'country': None,
            'tracks': []
        })
    
    country = spotify_client.iso_to_country_name(country_code)
    if country == None:
        return json.dumps({
            'country': None,
            'tracks': []
        })

    result = db.query("SELECT * FROM location_cache WHERE country_code = %s;", (country_code,))

    if result and result[0]['updated_at'] and result[0]['updated_at'] > datetime.now(timezone.utc) - timedelta(days=3):
        top_tracks = result[0]['top_tracks']
        return json.dumps({
            'country': spotify_client.iso_to_country_name(country_code),
            'tracks': top_tracks
        })
    else:
        top_tracks = spotify_client.get_coordinates_to_songs(lat, lon)
        updated_at = datetime.now(timezone.utc)

        if result:
            update_query = """
                UPDATE location_cache
                SET top_tracks = %s, updated_at = %s
                WHERE country_code = %s;
            """
            params = (Json(top_tracks), updated_at, country_code)
            db.query(update_query, params)
        else:
            insert_query = """
                INSERT INTO location_cache (country_code, top_tracks, updated_at)
                VALUES (%s, %s, %s);
            """
            params = (country_code, Json(top_tracks), updated_at)
            db.query(insert_query, params)

        return json.dumps({
            'country': spotify_client.iso_to_country_name(country_code),
            'tracks': top_tracks
        })