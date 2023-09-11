#!/usr/bin/node
/**
 * a script that printn two arguments passed to it
 */
const { argv } = require('process');

console.log(`${argv[2]} is ${argv[3]}`);
