#!/usr/bin/node
/**
 * a script that prints all characters of a star wars
 */
const { argv } = require('process');
const request = require('request');

request(`https://swapi-api.alx-tools.com/api/films/${argv[2]}`, (err, response, body) => {
  if (!err && response.statusCode === 200) {
    const movie = JSON.parse(body);
    const characterURL = movie.characters;
    printCharacters(characterURL, 0);
  }
});

function printCharacters (urls, index) {
  if (index < urls.length) {
    request(urls[index], (err, response, body) => {
      if (!err && response.statusCode === 200) {
        const character = JSON.parse(body);
        console.log(character.name);
        printCharacters(urls, index + 1);
      }
    });
  }
}
