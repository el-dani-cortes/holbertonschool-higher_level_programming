#!/usr/bin/node
/* Script that computes and prints a factorial */
function factorial (num) {
  if (num >= 1) {
    return (num * factorial(num - 1));
  } else {
    return 1;
  }
}
const args = process.argv;
if (args.length !== 3) {
  console.log(1);
} else {
  const num = parseInt(args[2]);
  if (isNaN(num)) {
    console.log(1);
  } else {
    console.log(factorial(num));
  }
}
