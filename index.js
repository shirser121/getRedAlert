const express = require('express');
const fetch = require('node-fetch');

const app = express();
const apiUrl = 'https://api.tzevaadom.co.il/alerts-history/';
let jsonData = null;

const updateData = async () => {
  try {
    const response = await fetch(apiUrl);
    const data = await response.json();
    jsonData = data;
  } catch (error) {
    console.error('Error:', error);
  }
};

app.get('/', (req, res) => {
  res.json(jsonData);
});

updateData();
// Update data every 10 seconds
setInterval(updateData, 10000);

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
