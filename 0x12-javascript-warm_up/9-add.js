#!/usr/bin/node
// find sum of two numbers
const num1 = Number(process.argv[2]);
const num2 = Number(process.argv[3]);
function sum (num1, num2) { return num1 + num2; }

if (isNaN(num1) || isNaN(num2)) {
  console.log('NaN');
} else {
  const total = sum(num1, num2);
  console.log(total);
}
