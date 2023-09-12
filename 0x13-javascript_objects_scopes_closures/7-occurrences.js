#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, val) => (val === searchElement ? count + 1 : count), 0);
};
