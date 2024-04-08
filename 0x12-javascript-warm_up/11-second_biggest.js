#!/usr/bin/node
// find 2nd biggest number in list

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const newList = process.argv.slice(2, process.argv.length + 1);
  newList.sort(function (a, b) { return a - b; });
  console.log(newList[1]);
}
