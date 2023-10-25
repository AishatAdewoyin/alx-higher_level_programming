#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.hbtn.io/api/films/';

request.get(apiUrl + movieId, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const movieData = JSON.parse(body);
  const characterUrls = movieData.characters;
  characterUrls.forEach((characterUrl) => {
    request.get(characterUrl, (characterError, characterResponse, characterBody) => {
      if (characterError) {
        console.error(characterError);
        return;
      }
      const characterData = JSON.parse(characterBody);
      console.log(characterData.name);
    });
  });
});
