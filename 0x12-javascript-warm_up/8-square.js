#!/usr/bin/node
/**
 * a script that prints a square
 */
const { argv } = require('process');
const x = parseInt(argv[2], 10);

if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    for (let j = 0; j < x; j++) process.stdout.write('X');
    console.log();
  }
}
