#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const film of films) {
      const filmChars = film.characters;
      for (const characterUrl of filmChars) {
        if (characterUrl.includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.error(`An error occurred. Status code: ${response.statusCode}`);
  }
});
