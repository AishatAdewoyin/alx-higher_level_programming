#!/usr/bin/node

const data = require('./100-data');
const dataList = data.list;

const output = dataList.map((value, index) => value * index);

console.log(dataList);
console.log(output);
