#!/usr/bin/node
/**
 * a script that prints all characters of a star wars movie
 */
const { argv } = require('process');
const request = require('request');

request(`https://swapi-api.alx-tools.com/api/films/${argv[2]}`, function (err, response, body) {
  if (!err && response.statusCode === 200) {
    const movie = JSON.parse(body);
    movie.characters.forEach((characterURL) => {
      request(characterURL, (err, response, body) => {
        if (!err && response.statusCode === 200) {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    });
  }
});
