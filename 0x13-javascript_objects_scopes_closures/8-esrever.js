#!/usr/bin/node
exports.esrever = function (list) {
  const length = list.length;
  for (let i = 0; i < length / 2; i++) {
    const temp = list[i];
    list[i] = list[length - i - 1];
    list[length - i - 1] = temp;
  }
  return list;
};
