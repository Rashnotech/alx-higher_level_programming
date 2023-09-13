#!/usr/bin/node
exports.converter = function (base) {
  return function convertToBase (value) {
    if (value === 0) {
      return '0';
    } else if (value < base) {
      return value.toString(16);
    } else {
      return convertToBase(Math.floor(value / base)) + (value % base).toString(16);
    }
  };
};
