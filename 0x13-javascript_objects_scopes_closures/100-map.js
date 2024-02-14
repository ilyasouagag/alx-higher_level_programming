#!/usr/bin/node
const list = require('./100-data.js');
console.log(list);
const newList = list.map((item, index) => item * index);
console.log(newList);
