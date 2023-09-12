#!/usr/bin/node
/**
 * a script that print x times
 */
const { argv } = require('process');
const x = parseInt(argv[2], 10);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) console.log('C is fun');
}
