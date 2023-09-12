#!/usr/bin/node

const argument = process.argv[2];

if (argument === null) {
  console.log('No arguments');
} else {
  console.log(argument);
}
