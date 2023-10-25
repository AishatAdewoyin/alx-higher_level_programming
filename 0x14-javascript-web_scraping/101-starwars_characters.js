#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

function printCharacters(characters, index) {
  if (index >= characters.length) {
    return;
  }

  request(characters[index], (error, response, body) => {
    if (!error) {
      const characterName = JSON.parse(body).name;
      console.log(characterName);
      printCharacters(characters, index + 1);
    }
  });
}

request(apiUrl, (error, response, body) => {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});
