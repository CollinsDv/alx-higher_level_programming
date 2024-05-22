#!/usr/bin/node
/*
script that reads and prints the contents of a file
  * The first argument is the file path
  * The content of the file must be read in utf-8
  * If an error occurred during the reading, print the error object
*/

const fs = require('node: fs');

fs.readFile(process.argv[2], (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});