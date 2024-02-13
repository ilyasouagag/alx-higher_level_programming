#!/usr/bin/node
function fact (a) {
  if (a === 0) {
    return 1;
  }
  return a * fact(a - 1);
}
if (process.argv[2] === undefined) {
  console.log('1');
} else {
  console.log(fact(parseInt(process.argv[2])));
}
