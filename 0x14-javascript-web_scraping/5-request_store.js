#!/usr/bin/node
// Script that gets the contents of a webpage and stores it in a file
const request = require('request');
const fs = require('fs');

// Get just the command line arguments needed: url to get the content
const url = process.argv[2];
const filename = process.argv[3];

// Print the number of movies where the character Wedge Antilles is present.
request(url, function (error, response, body) {
  if (error != null) {
    console.error('error:', error); // Print the error if one occurred
  }
  const content = body; // Get the content

  // Save content in a file
  fs.writeFile(filename, content, err => {
    if (err) {
      console.error(err);
    }
  });
});
