#!/usr/bin/node
/* Script that prints a square */
const args = process.argv;
if (args.length !== 3) {
  console.log('Missing size');
} else {
  const size = parseInt(args[2]);
  if (isNaN(size)) {
    console.log('Missing size');
  } else {
    let i;
    let j;
    let line;
    for (i = 0; i < size; i++) {
      line = 'X';
      for (j = 0; j < size - 1; j++) {
        line += 'X';
      }
      console.log(line);
    }
  }
}
