#!/usr/bin/node

const numberOfArguments = process.argv.length;

if (numberOfArguments === 0) {
  console.log('No arguments');
} else if (numberOfArguments === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
