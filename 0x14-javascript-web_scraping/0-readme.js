#!/usr/bin/node
/**
 * a script that reads and prints the content of a file
 */
const { argv } = require('process');
const fs = require('fs');

try {
  const readfile = fs.readFileSync(argv[2], 'utf-8');
  console.log(readfile);
} catch (e) {
  console.log(e);
}
