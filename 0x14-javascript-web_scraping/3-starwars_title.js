#!/usr/bin/node
/**
 * a script that prints the title of a star wars
 */
const { argv } = require('process');
const request = require('request');

request('https://swapi-api.alx-tools.com/api/films/' + argv[2],
  function (error, response, body) {
    if (!error && response.statusCode === 200) {
      const movie = JSON.parse(body);
      console.log(movie.title);
    } else {
      console.error('Error: Unable to fetch movie data');
    }
  });
