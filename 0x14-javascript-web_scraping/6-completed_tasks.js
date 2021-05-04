#!/usr/bin/node
// Script that computes the number of tasks completed by user id
const request = require('request');

// Get just the command line arguments needed: url to get the todos
const url = process.argv[2];

// Get and prints the number of tasks completed by user id
request(url, function (error, response, body) {
  if (error != null) {
    console.error('error:', error); // Print the error if one occurred
  }
  const content = JSON.parse(body); // Get all todos by user ids
  const users = [];
  content.forEach(item => {
    if (users.includes(item.userId) !== true) {
      users.push(item.userId);
    }
  });
  const result = {};
  users.forEach(item => {
    let counter = 0;
    content.forEach(element => {
      if (item === element.userId && element.completed === true) {
        counter += 1;
      }
    });
    result[item] = counter;
  });
  console.log(result);
});
