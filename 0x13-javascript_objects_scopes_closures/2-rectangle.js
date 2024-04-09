#!/usr/bin/node
// create a class. If w or h is < 0, create an empty class
module.exports = class Rectangle {
  width;
  height;
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      // empty instance created
    } else {
      this.width = w;
      this.height = h;
    }
  }
};
