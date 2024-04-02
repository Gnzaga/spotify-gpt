import React, { useState } from 'react';
import axios from 'axios';
import './index.css';

function App() {
  const [playlistUrl, setPlaylistUrl] = useState('');
  const [sampleWords, setSampleWords] = useState('');
  const [imageURL, setImageURL] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setIsLoading(true);
    setImageURL('');

    const apiUrl = 'http://localhost:5000/generate-playlist-image';

    try {
      const response = await axios.post(apiUrl, {
        url: playlistUrl,
        sample_word: sampleWords,
      });
      setImageURL(response.data.image_url); 
    } catch (error) {
      console.error('There was an error generating the playlist image:', error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="bg-spotify-dark text-spotify-light min-h-screen flex flex-col items-center pt-10">
      <h1 className="text-4xl font-bold text-spotify-green mb-6">Generate Playlist Image</h1>
      <form onSubmit={handleSubmit} className="w-full max-w-md">
        <div className="mb-4">
          <label htmlFor="playlistUrl" className="block text-spotify-grey text-lg font-medium mb-2">Playlist URL:</label>
          <input
            id="playlistUrl"
            type="text"
            value={playlistUrl}
            onChange={(e) => setPlaylistUrl(e.target.value)}
            className="appearance-none block w-full bg-spotify-dark text-spotify-light border border-spotify-grey rounded-md py-3 px-4 leading-tight focus:outline-none focus:bg-black focus:border-spotify-green"
          />
        </div>
        <div className="mb-6">
          <label htmlFor="sampleWords" className="block text-spotify-grey text-lg font-medium mb-2">Sample Words:</label>
          <input
            id="sampleWords"
            type="text"
            value={sampleWords}
            onChange={(e) => setSampleWords(e.target.value)}
            className="appearance-none block w-full bg-spotify-dark text-spotify-light border border-spotify-grey rounded-md py-3 px-4 leading-tight focus:outline-none focus:bg-black focus:border-spotify-green"
          />
        </div>
        <button type="submit" disabled={isLoading} className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-lg font-medium text-black bg-spotify-green hover:bg-green-800 focus:outline-none focus:ring-2 focus:ring-spotify-green focus:ring-opacity-50 transition duration-150 ease-in-out">
          {isLoading ? 'Loading...' : 'Generate Image'}
        </button>
      </form>
      {imageURL && (
        <div className="mt-8 text-center">
          <h2 className="text-2xl font-semibold text-spotify-green mb-4">Generated Image:</h2>
          <div className="px-[15%]">
          <img src={imageURL} alt="Generated from Playlist" className="max-w-full rounded-md shadow-lg" />

          <h3 className="text-lg font-medium text-spotify-grey mt-4">Image URL:</h3>
          <a href={imageURL} target="_blank" rel="noopener noreferrer" className="text-spotify-green hover:underline">{imageURL}</a>
          <div className="mt-4">
          </div>
            
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
