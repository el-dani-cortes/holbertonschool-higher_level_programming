#!/usr/bin/node
// Script that reads and prints the content of a file

// Get just the command line arguments needed, filepath
const argvs = process.argv.slice(2);
const filename = argvs[0];

// Read a file and print to the stdout
const fs = require('fs');
fs.readFile(filename, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
