#!/usr/bin/node
// We can't use length, so we check whether the first argument exists
const first = process.argv[2];

if (first === undefined) {
  console.log('No argument');
} else {
  console.log(first);
}
