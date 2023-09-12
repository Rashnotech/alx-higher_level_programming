#!/usr/bin/node
/**
 * a script that prints number
 */
const { argv } = require('process');
const integer = parseInt(argv[2], 10);
if (!isNaN(integer)) {
  console.log(`My number: ${integer}`);
} else {
  console.log('Not a number');
}
