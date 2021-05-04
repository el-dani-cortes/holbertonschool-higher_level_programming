#!/usr/bin/node
// Script that prints the title of a Star Wars movie where the episode number matches a given integer
const request = require('request');

// Get just the command line arguments needed: Id of the episode Star Wars movie.
const id = process.argv[2];
const API = 'https://swapi-api.hbtn.io/api/films/' + id;

// Print the title of Star Wars Movie
request(API, function (error, response, body) {
  if (error != null) {
    console.error('error:', error); // Print the error if one occurred
  }
  const objMovie = JSON.parse(body); // Parse the string json to a object
  console.log(objMovie.title);
});
