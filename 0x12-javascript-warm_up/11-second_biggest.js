#!/usr/bin/node
if (process.argv[2] === undefined || process.argv.length === 3) {
  console.log('0');
} else {
  let max = 0;
  for (let i = 3; i < process.argv.length - 2; i++) {
    max = process.argv[2];
    if (process.argv[i] > max) {
      max = process.argv[i];
    }
  }
  console.log(max);
}
