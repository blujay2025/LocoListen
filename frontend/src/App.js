import { useState } from 'react';
import MapComponent from './MapComponent';
import TrackTable from './TrackTable';
import axios from 'axios';
import './App.css';

function App() {
  const [tracks, setTracks] = useState([]);
  const [country, setCountry] = useState('');
  const [loading, setLoading] = useState(false);

  const handleMapClick = async (lat, lon) => {
    setLoading(true);
    setTracks([]);
    setCountry('');

    try {
      const response = await axios.post('/get-top-tracks', null, {
        params: {
          latitude: lat,
          longitude: lon,
        },
      });

      const data = response.data;
      setTracks(data.tracks);
      setCountry(data.country);
    } catch (error) {
      console.error('Failed to fetch top tracks:', error);
      setTracks([]);
      setCountry('');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <header className="app-header">
        <h1>LocoListen 🌍</h1>
        <p>Click on any location to discover the top 50 songs in that country!</p>
      </header>

      <MapComponent onLocationClick={handleMapClick} />

      {loading ? (
        <div className="loading-container">
          <div className="spinner" />
          <p>Fetching music data...</p>
        </div>
      ) : (
        <TrackTable tracks={tracks} country={country} />
      )}
    </div>
  );
}

export default App;