#!/usr/bin/node
/**
 * a scrpt that prints the first argument passed to it
 */
const { argv } = require('process');

if (argv.length === 3) {
  console.log(argv[2]);
} else {
  console.log('No argument');
}
