#!/usr/bin/node
// script that prints all characters of a Star Wars movie:
// The first positional argument passed is the Movie ID
//    example: 3 = “Return of the Jedi”
// Display one character name per line in the same order as the “characters”
//    list in the /films/ endpoint
// You must use the Star wars API
// You must use the request module

const request = require('request');
const util = require('util');
const getRequest = util.promisify(request);

const movieId = process.argv[2];
const API = 'https://swapi-api.alx-tools.com';

function getCharacterNames (movieId) {
  return new Promise(async (resolve, reject) => {
    try {
      const { body } = await getRequest(`${API}/api/films/${movieId}/`);
      const characters = JSON.parse(body).characters;
      const characterNames = [];

      for (const character of characters) {
        const { body } = await getRequest(character);
        characterNames.push(JSON.parse(body).name);
      }

      resolve(characterNames.join('\n'));
    } catch (error) {
      reject(`Error: ${error}`);
    }
  });
}

getCharacterNames(process.argv[2])
  .then(console.log)
  .catch(console.error);
