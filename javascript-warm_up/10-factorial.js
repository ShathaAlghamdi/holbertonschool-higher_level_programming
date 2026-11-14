#!/usr/bin/node
// Recursive: n! = n * (n - 1)!, and the stopping case returns 1
function factorial (n) {
  if (isNaN(n) || n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

console.log(factorial(parseInt(process.argv[2])));
