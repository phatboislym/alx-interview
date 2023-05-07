#!/usr/bin/node
// script that prints all characters of a Star Wars movie:
// The first positional argument passed is the Movie ID
//    example: 3 = “Return of the Jedi”
// Display one character name per line in the same order as the “characters”
//    list in the /films/ endpoint
// You must use the Star wars API
// You must use the request module

const request = require('request');
const movieId = process.argv[2];

request(`https://swapi.dev/api/films/${movieId}/`, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error}`);
  } else {
    const characters = JSON.parse(body).characters;
    const characterNames = [];
    let index = 0;

    const makeRequest = () => {
      if (index < characters.length) {
        request(characters[index], (error, response, body) => {
          if (error) {
            console.error(`Error: ${error}`);
          } else {
            const character = JSON.parse(body);
            characterNames.push(character.name);
          }

          index++;
          makeRequest();
        });
      } else {
        console.log(characterNames.join('\n'));
      }
    };

    makeRequest();
  }
});
