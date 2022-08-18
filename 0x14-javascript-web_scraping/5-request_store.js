#!/usr/bin/node
const url = process.argv[2];
const filePath = process.argv[3];
const request = require('request');
const fs = require('fs');
request(url, function (err, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(filePath, body, function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
