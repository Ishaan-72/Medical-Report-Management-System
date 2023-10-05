const express = require('express');
const app = express();

// Serve static files in the "public" folder
app.use(express.static('PUBLIC'));

// Serve index.html on the homepage
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

// Start the server
app.listen(3000, () => {
  console.log('Server started on port 3000');
});


