#!/usr/bin/node
// prints number of arguments already printed

let index = 0;
exports.logMe = function (item) {
  console.log(`${index}: ${item}`);
  index++;
};
