import { MapContainer, TileLayer, useMapEvents } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';

function LocationMarker({ onClickLocation }) {
  useMapEvents({
    click(e) {
      const { lat, lng } = e.latlng;
      onClickLocation(lat, lng);
    },
  });

  return null;
}

export default function MapComponent({ onLocationClick }) {
  return (
    <MapContainer
      center={[20, 0]}
      zoom={2}
      maxBounds={[[-90, -180], [90, 180]]}
      maxBoundsViscosity={1.0}
      style={{
        height: '500px',
        width: '100%',
        marginBottom: '20px',
        border: '2px solid black',
        borderRadius: '8px',
      }}
    >
      <TileLayer
        attribution='&copy; OpenStreetMap contributors'
        url='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
        noWrap={true}
        bounds={[[-90, -180], [90, 180]]}
      />
      <LocationMarker onClickLocation={onLocationClick} />
    </MapContainer>
  );
}