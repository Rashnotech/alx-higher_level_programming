#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
for (const id in dict) {
  const samp = dict[id];
  if (newDict[samp] === undefined) {
    newDict[samp] = [];
  }
  newDict[samp].push(id);
}
console.log(newDict);
