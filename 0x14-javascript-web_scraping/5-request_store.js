#!/usr/bin/node
/*
gets webpage contents and stores in a file
- 1st arg: URL request
- 2nd arg: file path (UTF-8 encoded)
- use request module
*/

const request = require('request');
const fs = require('fs');

request(process.argv[2], (_err, _res, body) => {
  fs.writeFile(process.argv[3], body, 'utf8', (err) => {
    if (err) {
      console.log(err);
    }
  });
});
