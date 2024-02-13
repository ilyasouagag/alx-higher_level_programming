#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
}
for (let i = 0; i < process.argv[2]; i++) {
  for (let j = 0; j < process.argv[2]; j++) {
    process.stdout.write('X');
  }
  console.log('');
}
