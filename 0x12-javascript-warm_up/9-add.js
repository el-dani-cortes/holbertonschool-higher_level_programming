#!/usr/bin/node
/* Script that prints the addition of 2 integers */
function add (a, b) {
  return (a + b);
}
const args = process.argv;
if (args.length !== 4) {
  console.log('NaN');
} else {
  const a = parseInt(args[2]);
  const b = parseInt(args[3]);
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    console.log(add(a, b));
  }
}
