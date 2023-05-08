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

const API = 'https://swapi-api.alx-tools.com';
const movieId = process.argv[2];
const getRequest = util.promisify(request);

async function getCharacterNames (movieId) {
  try {
    const { body } = await getRequest(`${API}/api/films/${movieId}/`);
    const characters = JSON.parse(body).characters;
    const characterNames = [];

    for (const character of characters) {
      const { body } = await getRequest(character);
      characterNames.push(JSON.parse(body).name);
    }

    console.log(characterNames.join('\n'));
  } catch (error) {
    console.error(`Error: ${error}`);
  }
}

getCharacterNames(movieId);
