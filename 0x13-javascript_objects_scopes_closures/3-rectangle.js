#!/usr/bin/node
// create a class. If w or h is < 0, create an empty class, with a print function
module.exports = class Rectangle {
  width;
  height;
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      return {};
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write('X');
        if (j === this.width - 1) { process.stdout.write('\n'); }
      }
    }
  }
};
