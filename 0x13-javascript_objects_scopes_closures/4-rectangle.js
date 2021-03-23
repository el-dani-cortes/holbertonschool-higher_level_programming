#!/usr/bin/node
/* Class Rectangle that defines a rectangle  */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Method to print a rectangle image with "X"
  print () {
    let line;
    for (let i = 0; i < this.height; i++) {
      line = 'X';
      for (let j = 0; j < this.width - 1; j++) {
        line += 'X';
      }
      console.log(line);
    }
  }

  // Method that exchanges the width and the height of the rectangle
  rotate () {
    const a = this.width;
    this.width = this.height;
    this.height = a;
  }

  // Method that multiples the width and the height of the rectangle by 2
  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
