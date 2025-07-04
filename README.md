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
  
Created by Ajay Kumar: <ajay.kumar.6703@gmail.com>
