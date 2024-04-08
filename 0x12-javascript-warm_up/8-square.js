#!/usr/bin/node
// prints a square if argv[2] is not NaN
const width = Number(process.argv[2]);
if (isNaN(width)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < width; i++) {
    for (let j = 0; j < width; j++) {
      process.stdout.write('X');
      if (j === width - 1) { process.stdout.write('\n'); }
    }
  }
}
