#!/usr/bin/node
/*
Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.

* The first argument is the movie ID
* You must use the Star Wars API with the endpoint https://swapi-api.alx-tools.com/api/films/:id
* You must use the module request
*/

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const movie = JSON.parse(body);
    console.log(movie.title);
  } else {
    console.log('Error:', error || `Status code: ${response.statusCode}`);
  }
});
