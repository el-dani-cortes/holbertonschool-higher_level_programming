#!/usr/bin/node
// Script that prints the number of movies where the character Wedge Antilles is present.
const request = require('request');

// Get just the command line arguments needed: API url of Star Wars
const API = process.argv[2];

// Print the number of movies where the character Wedge Antilles is present.
request(API, function (error, response, body) {
  if (error != null) {
    console.error('error:', error); // Print the error if one occurred
  }
  const objMovie = JSON.parse(body); // Parse the string json to a object
  let count = 0;
  objMovie.results.forEach(element => {
    element.characters.forEach(item => {
      if (item === 'https://swapi-api.hbtn.io/api/people/18/') {
        count += 1;
      }
    });
  });
  console.log(count);
});
