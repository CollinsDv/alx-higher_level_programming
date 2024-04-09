#!/usr/bin/node
const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          process.stdout.write('c');
          if (j === this.width - 1) { process.stdout.write('\n'); }
        }
      }
    }
  }
}

module.exports = Square;
