#!/usr/bin/node
/**
 * a scrpt that prints the first argument passed to it
 */
const { argv } = require('process');

if (argv.length === 2) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
