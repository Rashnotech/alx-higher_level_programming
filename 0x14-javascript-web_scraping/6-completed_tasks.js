#!/usr/bin/node
/**
 * a script that computes the number of task completed
 */
const { argv } = require('process');
const request = require('request');

const completed = {};
request(argv[2], function (err, response, body) {
  if (!err && response.statusCode === 200) {
    const todos = JSON.parse(body);
    for (const todo of todos) {
      if (todo.completed) {
        if (!completed[todo.userId]) {
          completed[todo.userId] = 1;
        } else {
          completed[todo.userId]++;
        }
      }
    }
    console.log(completed);
  } else {
    console.log('Unable to fetch data');
  }
});
