#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get(url, (err, response, body) => {
  if (err) {
    console.error('error:', err);
  }
  const data = JSON.parse(body);
  data.characters.forEach((char) => {
    request.get(char, (err1, response1, body1) => {
      if (err1) {
        console.error('error:', err1);
      }
      const OneCharacter = JSON.parse(body1);
      console.log(OneCharacter.name);
    });
    return 0;
  });
});
