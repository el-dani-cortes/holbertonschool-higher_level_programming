#!/usr/bin/node
/* Script that prints x times "C is fun" */
const args = process.argv;
if (args.length !== 3 || isNaN(parseInt(args[2]))) {
  console.log('Missing number of occurrences');
} else {
  let num = parseInt(args[2]);
  while (num > 0) {
    console.log('C is fun');
    num--;
  }
}
