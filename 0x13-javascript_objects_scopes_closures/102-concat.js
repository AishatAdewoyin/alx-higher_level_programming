#!/usr/bin/node

const fs = require('fs');

const [file1, file2, destinationFile] = process.argv.slice(2);
const concatContent = fs.readFileSync(file1, 'utf-8') + fs.readFileSync(file2, 'utf-8');
fs.writeFileSync(destinationFile, concatContent);
