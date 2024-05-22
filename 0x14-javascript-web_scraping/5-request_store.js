#!/usr/bin/node
/*
gets webpage contents and stores in a file
- 1st arg: URL request
- 2nd arg: file path (UTF-8 encoded)
- use request module
*/

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error('Error: Failed to fetch data. Status code:', response.statusCode);
    return;
  }
  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) {
      console.error('Error writing to file:', err);
    }
  });
});
