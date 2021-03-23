#!/usr/bin/node
/*  Class Square that defines a square and inherits from Rectangle */
const _square = require('./5-square');
class Square extends _square {
  constructor (size) {
    super(size, size);
  }

  // Method that prints the rectangle using the character "C" or "X"
  charPrint (c) {
    if (c) {
      let line;
      for (let i = 0; i < this.height; i++) {
        line = c;
        for (let j = 0; j < this.width - 1; j++) {
          line += c;
        }
        console.log(line);
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square;
