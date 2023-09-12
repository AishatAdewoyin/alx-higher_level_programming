#!/usr/bin/node

const data = require('./101-data');
const dataDict = data.dict;

const userDict = {};

for (const userId in dataDict) {
  const userDataDict = dataDict[userId];

  if (!userDict[userDataDict]) {
    userDict[userDataDict] = [];
  }

  userDict[userDataDict].push(userId);
}

console.log(userDict);
