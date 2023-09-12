#!/usr/bin/node
/**
 * a script that searches the second biggest integer
 */
const { argv } = require('process');
let xsMax = 0;
if (argv.length <= 3) {
  xsMax = 0;
} else {
  let max = parseInt(argv[2], 10);
  for (let i = 0; i < argv.length; i++) {
    const num = parseInt(argv[i], 10);
    if (num > max) {
      xsMax = max;
      max = num;
    } else if (num > xsMax && num < max) {
      xsMax = num;
    }
  }
}
console.log(xsMax);
