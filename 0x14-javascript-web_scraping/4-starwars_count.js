#!/usr/bin/node
/**
 * a script that prints the title of a star wars
 */
const { argv } = require('process');
const request = require('request');

let count = 0;

request(argv[2], function (error, response, body) {
  if (!error && response.statusCode === 200) {
    for (const movie of JSON.parse(body).results) {
      const characters = movie.characters;
      for (const list of characters) {
        if (list.endsWith('/18/')) count++;
      }
    }
  } else {
    console.error('Error: Unable to fetch movie data');
  }
  console.log(count);
});
