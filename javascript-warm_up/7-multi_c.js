#!/usr/bin/node
const x = parseInt(process.argv[2]);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  // A negative or zero x simply prints nothing
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
