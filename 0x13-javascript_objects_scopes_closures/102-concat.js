#!/usr/bin/node
const fs = require('fs');

function concat (file1, file2, dest) {
  const source1 = fs.readFileSync(file1, 'utf-8');
  const source2 = fs.readFileSync(file2, 'utf-8');
  const combine = source1 + source2;
  fs.writeFileSync(dest, combine);
}

if (process.argv.length !== 5) {
  console.error('Usage: node.js file1 file2 dest');
  process.exit(1);
}

const sF1 = process.argv[2];
const sF2 = process.argv[3];
const destFile = process.argv[4];

if (!fs.existsSync(sF1) || !fs.existsSync(sF2)) {
  console.error('Source file(s) do not exist.');
  process.exit(1);
}

concat(sF1, sF2, destFile);
