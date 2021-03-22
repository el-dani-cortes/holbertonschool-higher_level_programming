#!/usr/bin/node
/*
* Script that prints 3 lines: (like 1-multi_languages.js)
* but by using an array of string and a loop.
*/
const myvar = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let i = 0;
while (i < myvar.length) {
  console.log(myvar[i]);
  i++;
}
