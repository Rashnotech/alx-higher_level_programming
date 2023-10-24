#!/usr/bin/node
/**
 * a script that display the status code of a GET request
 */
const fs = require('fs');
const { argv } = require('process');
const request = require('request');

request.get(argv[2]).on('response', function(response) {
  console.log('code:', response.statusCode);
});
