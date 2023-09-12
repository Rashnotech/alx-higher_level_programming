#!/usr/bin/node
/**
 * a script that computes and prints a factorial
 */
const { argv } = require('process');
const x = parseInt(argv[2], 10);

function factorial (a) {
  if (a === 1 || isNaN(x)) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}
console.log(factorial(x));
