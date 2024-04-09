#!/usr/bin/node
// func visible from outside module,  has to be named add
exports.add = function (num1, num2) {
  return num1 + num2;
};
