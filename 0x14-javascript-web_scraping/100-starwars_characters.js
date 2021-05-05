#!/usr/bin/node
// Script that prints the number of movies where the character Wedge Antilles is present.
const request = require('request');

// Get just the command line arguments needed: Id  of Star Wars
const idFilm = process.argv[2];

// API of StarWars used to get all info about characters by film id
const API = 'https://swapi-api.hbtn.io/api/films/' + idFilm;

// Print the number of movies where the character Wedge Antilles is present.
request(API, function (error, response, body) {
  if (error != null) {
    console.error('error:', error); // Print the error if one occurred
  }
  const objFilm = JSON.parse(body); // Parse the string json to a object
  objFilm.characters.forEach(element => {
    request(element, function (error, response, body) {
      if (error != null) {
        console.error('error:', error); // Print the error if one occurred
      }
      const objActor = JSON.parse(body);
      console.log(objActor.name);
    });
  });
});
