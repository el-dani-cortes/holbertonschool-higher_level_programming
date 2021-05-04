#!/usr/bin/node
// Script that display the status code of a GET request.
const request = require('request');

// Get just the command line arguments needed: url to get the status code
const url = process.argv[2];

// Print the status from the request url page
request(url, function (error, response) {
  if (error != null) {
    console.error('error:', error);
    return;
  }
  console.log('code:', response && response.statusCode); // Print the response status code if a response was received
});
