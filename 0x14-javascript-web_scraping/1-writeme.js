#!/usr/bin/node
// Script that creates and file with a content

// Get just the command line arguments needed: filepath and string content
const argvs = process.argv.slice(2);
const filename = argvs[0];
const content = argvs[1];

// Write a content in a file
const fs = require('fs');
fs.writeFile(filename, content, err => {
  if (err) {
    console.error(err);
  }
});
