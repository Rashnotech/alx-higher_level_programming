#!/usr/bin/node
exports.converter = function (base) {
  return function (value) {
    if (value === 0) {
      return '0';
    }

    let result = '';
    while (value !== 0) {
      result = (value % base).toString(16) + result;
      value = Math.floor(value / base);
    }
    return result;
  };
};
