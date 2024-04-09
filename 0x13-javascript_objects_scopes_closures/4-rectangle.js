#!/usr/bin/node
// additional functions to switch variable content and double them

class Rectangle {
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

  // switch
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // double
  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
