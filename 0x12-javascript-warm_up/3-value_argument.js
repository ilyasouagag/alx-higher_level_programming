#!/usr/bin/node
const args = process.argv.length - 2;
if (args === 0) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
