#!/usr/bin/node
/**
 * a script that gets the contents of a webpage
 * and stores it in a file
 */
const { argv } = require('process');
const request = require('request');
const fs = require('fs');

request(argv[2], function (error, response, body) {
  if (!error && response.statusCode === 200) {
    fs.writeFileSync(argv[3], body, 'utf-8');
  } else {
    console.error('Unable to fetch data');
  }
});
