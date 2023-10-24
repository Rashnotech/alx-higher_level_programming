#!/usr/bin/node
/**
 * a script that reads and prints the content of a file
 */
const { argv } = require('process');
const fs = require('fs');

try {
  const content = argv[3];
  fs.writeFileSync(argv[2], content);
} catch (e) {
  console.log(e);
}
