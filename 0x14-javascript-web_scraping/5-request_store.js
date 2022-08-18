#!/usr/bin/node
const url = process.argv[2];
const file = process.argv[3];
const fs = require('fs');
const request = require('request');
request(url, function (err, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(file, body, 'utf8');
  }
});
