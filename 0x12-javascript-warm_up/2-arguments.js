#!/usr/bin/node
/**
 * a script that prints a message depending of the number of args passed
 */

const { argv } = require('process');

if (argv.length === 2) {
  console.log('No argument');
} else if (argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
