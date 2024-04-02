module.exports = {
  purge: ['./src/**/*.{js,jsx,ts,tsx}', './public/index.html'],
  theme: {
    extend: {
      colors: {
        spotify: {
          dark: '#191414', // Spotify dark background
          green: '#1DB954', // Spotify brand green
          grey: '#b3b3b3', // Spotify text grey
          light: '#FFFFFF', // Light color for text
        },
      },
    },
  },
  plugins: [],
};
