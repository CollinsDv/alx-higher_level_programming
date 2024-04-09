#!/usr/bin/node
// create a class. If w or h is < 0, create an empty class
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      return {};
    }
  }
};
