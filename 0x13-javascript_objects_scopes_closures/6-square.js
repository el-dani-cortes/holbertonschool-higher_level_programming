#!/usr/bin/node
/*  Class Square that defines a square and inherits from Rectangle */
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  // Method that prints the rectangle using the character "C" or "X"
  charPrint (c) {
    if (c) {
      let line;
      for (let i = 0; i < this.height; i++) {
        line = 'C';
        for (let j = 0; j < this.width - 1; j++) {
          line += 'C';
        }
        console.log(line);
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square;
