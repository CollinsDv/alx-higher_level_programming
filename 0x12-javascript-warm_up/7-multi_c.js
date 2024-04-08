#!/usr/bin/node
// prints a string x times if argv[2] is not NaN
const num = Number(process.argv[2]);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num; i++) { console.log('C is fun'); }
}
