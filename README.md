# LocoListen

## Purpose:
The purpose of this application is to allow users to click on any location on the map and view the top 50 songs in that location. Now, how is that done? Well, when a user clicks on any location on the map, the latitude and longitude are used to find all the relevant top 50 song playlists there. From the available playlists, Google's Gemini 2.5 Pro model is used to pick the best, single playlist that captures the most accurate 50 songs specific to that location. A database is used in the backend to cache playlist data per country, so that Spotify API calls are only made every 3 days for a location's country (database retrieval of playlist data is a lot faster than hitting the Spotify API constantly). Hope you enjoy using LocoListen!

## Link to LocoListen:
- Feel free to check it out here: <http://ec2-13-220-81-222.compute-1.amazonaws.com:3000>

## Tech Stack:
- Backend: Flask
- Frontend: React.js
- Database: PostgreSQL (for playlist data caching per country)
- Containerization: Docker
- Cloud Hosting: Amazon Elastic Compute Cloud (Amazon EC2)
- APIs: Spotify (to retrieve playlists), Gemini (to filter the most accurate playlist from retrieved Spotify playlists), OpenCage (to convert latitude, longitude pairs into 2-digit ISO country codes)

## Important Notes (PLEASE READ!):
- Spotify's API only services a certain subset of countries, so if you click on any location whose country is not part of the following list, you will not see top 50 songs there. Here's the list of countries serviced by Spotify's API:
['Andorra', 'United Arab Emirates', 'Antigua and Barbuda', 'Albania', 'Armenia', 'Angola', 'Argentina', 'Austria', 'Australia', 'Azerbaijan', 'Bosnia and Herzegovina', 'Barbados', 'Bangladesh', 'Belgium', 'Burkina Faso', 'Bulgaria', 'Bahrain', 'Burundi', 'Benin', 'Brunei Darussalam', 'Bolivia, Plurinational State of', 'Brazil', 'Bahamas', 'Bhutan', 'Botswana', 'Belarus', 'Belize', 'Canada', 'Congo, The Democratic Republic of the', 'Congo', 'Switzerland', "Côte d'Ivoire", 'Chile', 'Cameroon', 'Colombia', 'Costa Rica', 'Cabo Verde', 'Curaçao', 'Cyprus', 'Czechia', 'Germany', 'Djibouti', 'Denmark', 'Dominica', 'Dominican Republic', 'Algeria', 'Ecuador', 'Estonia', 'Egypt', 'Spain', 'Ethiopia', 'Finland', 'Fiji', 'Micronesia, Federated States of', 'France', 'Gabon', 'United Kingdom', 'Grenada', 'Georgia', 'Ghana', 'Gambia', 'Guinea', 'Equatorial Guinea', 'Greece', 'Guatemala', 'Guinea-Bissau', 'Guyana', 'Hong Kong', 'Honduras', 'Croatia', 'Haiti', 'Hungary', 'Indonesia', 'Ireland', 'Israel', 'India', 'Iraq', 'Iceland', 'Italy', 'Jamaica', 'Jordan', 'Japan', 'Kenya', 'Kyrgyzstan', 'Cambodia', 'Kiribati', 'Comoros', 'Saint Kitts and Nevis', 'Korea, Republic of', 'Kuwait', 'Kazakhstan', "Lao People's Democratic Republic", 'Lebanon', 'Saint Lucia', 'Liechtenstein', 'Sri Lanka', 'Liberia', 'Lesotho', 'Lithuania', 'Luxembourg', 'Latvia', 'Libya', 'Morocco', 'Monaco', 'Moldova, Republic of', 'Montenegro', 'Madagascar', 'Marshall Islands', 'North Macedonia', 'Mali', 'Mongolia', 'Macao', 'Mauritania', 'Malta', 'Mauritius', 'Maldives', 'Malawi', 'Mexico', 'Malaysia', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Nicaragua', 'Netherlands', 'Norway', 'Nepal', 'Nauru', 'New Zealand', 'Oman', 'Panama', 'Peru', 'Papua New Guinea', 'Philippines', 'Pakistan', 'Poland', 'Puerto Rico', 'Palestine, State of', 'Portugal', 'Palau', 'Paraguay', 'Qatar', 'Romania', 'Serbia', 'Rwanda', 'Saudi Arabia', 'Solomon Islands', 'Seychelles', 'Sweden', 'Singapore', 'Slovenia', 'Slovakia', 'Sierra Leone', 'San Marino', 'Senegal', 'Suriname', 'Sao Tome and Principe', 'El Salvador', 'Eswatini', 'Chad', 'Togo', 'Thailand', 'Tajikistan', 'Timor-Leste', 'Tunisia', 'Tonga', 'Türkiye', 'Trinidad and Tobago', 'Tuvalu', 'Taiwan, Province of China', 'Tanzania, United Republic of', 'Ukraine', 'Uganda', 'United States', 'Uruguay', 'Uzbekistan', 'Saint Vincent and the Grenadines', 'Venezuela, Bolivarian Republic of', 'Viet Nam', 'Vanuatu', 'Samoa', 'Kosovo', 'South Africa', 'Zambia', 'Zimbabwe']

- Sometimes, when the Spotify API is hit too many consequent times in a row, the resource gets exhausted, and you won't be able to see top 50 tracks data for a country. In this case, you might see the "spinning wheel of doom" on your screen for a while. If this is the case, come back after a while, and you should be able to see top 50 tracks data for countries of your choosing again.
  
  
Created by Ajay Kumar: <ajay.kumar.6703@gmail.com>
