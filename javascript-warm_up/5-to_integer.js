#!/usr/bin/node
// parseInt returns NaN when the text is not a number
const num = parseInt(process.argv[2]);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
