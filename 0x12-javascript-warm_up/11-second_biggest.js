#!/usr/bin/node
/**
 * a script that searches the second biggest integer
 */
const { argv } = require('process');
let xsMax = 0;
if (argv.length <= 3) {
  xsMax = 0;
} else {
  let max = argv[2];
  for (let i = 0; i < argv.length; i++) {
    if (argv[i] > max) {
      xsMax = max;
      max = argv[i];
    } else if (argv[i] > xsMax && argv[i] < max) {
      xsMax = argv[i];
    }
  }
}
console.log(xsMax);
