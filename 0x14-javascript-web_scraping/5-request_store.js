#!/usr/bin/node
/*
gets webpage contents and stores in a file
- 1st arg: URL request
- 2nd arg: file path(utf-8 encoded)
- use request module
*/

const request = require('request');
const fs = require('fs');

const _url = process.argv[2];
const _file = process.argv[3];

request(_url).pipe(fs.createWriteStream(_file));
