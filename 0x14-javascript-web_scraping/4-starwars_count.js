#!/usr/bin/node
/*
Write a script that prints the number of movies where the character “Wedge Antilles” is present.

* The first argument is the API URL of the Star Wars API: https://swapi-api.alx-tools.com/api/films/
* Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
* You must use the module request
*/

const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

request.get(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const film of films) {
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
        count++;
      }
    }
    console.log(count);
  } else {
    console.error('Error:', error || `Status code: ${response.statusCode}`);
  }
});