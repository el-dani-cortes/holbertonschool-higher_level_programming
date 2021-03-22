#!/usr/bin/node
/* Script that prints x times "C is fun" */
const args = process.argv;
if (args.length !== 3) {
  console.log('Missing number of occurrences');
} else {
  let num = parseInt(args[2]);
  if (isNaN(num)) {
    console.log('Missing number of occurrences');
  } else {
    while (num > 0) {
      console.log('C is fun');
      num--;
    }
  }
}
