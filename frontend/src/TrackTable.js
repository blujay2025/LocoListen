export default function TrackTable({ tracks, country }) {
  const hasTracks = tracks && tracks.length > 0;

  return (
    <div>
      <h2 style={{ textAlign: 'center' }}>
        {hasTracks ? `Top Tracks in ${country}` : "No Data Available!"}
      </h2>

      {hasTracks && (
        <table style={{ width: '100%', borderCollapse: 'collapse', marginTop: '20px', border: '2px solid black' }}>
          <thead>
            <tr>
              <th style={cellStyle}>Cover</th>
              <th style={cellStyle}>Song</th>
              <th style={cellStyle}>Artists</th>
              <th style={cellStyle}>Album</th>
            </tr>
          </thead>
          <tbody>
            {tracks.map((track, index) => (
              <tr key={index}>
                <td style={cellStyle}>
                  <img src={track.image} alt="Cover" width="60" />
                </td>
                <td style={cellStyle}>{track.name}</td>
                <td style={cellStyle}>{track.artists.join(', ')}</td>
                <td style={cellStyle}>{track.album}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}


const cellStyle = {
  border: '1px solid black',
  padding: '8px',
  textAlign: 'left',
  backgroundColor: '#ed8a82'
};