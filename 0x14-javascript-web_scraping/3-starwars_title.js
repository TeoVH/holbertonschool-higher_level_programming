#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const id = process.argv[2];
request(url + id, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const jsonObj = JSON.parse(body);
    console.log(jsonObj.title);
  }
});
