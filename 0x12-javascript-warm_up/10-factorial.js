#!/usr/bin/node
// prints factorial using recursion

const num = Number(process.argv[2]);

function fac (n) {
  if (n <= 1 || isNaN(n)) { return 1; }
  const product = n * fac(n - 1);
  return product;
}

console.log(fac(num));
