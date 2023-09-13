#!/usr/bin/node
const dict = require('./101-data').dict;
const new_dict = {};
for (const id in dict) {
  const samp = dict[id];
  if (new_dict[samp] === undefined) {
    new_dict[samp] = [];
  }
  new_dict[samp].push(id);
}
console.log(new_dict);
