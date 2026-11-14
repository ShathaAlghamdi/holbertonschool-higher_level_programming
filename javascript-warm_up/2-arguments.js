#!/usr/bin/node
// process.argv[0] is node, [1] is the script, real arguments start at [2]
const args = process.argv.slice(2);

if (args.length === 0) {
  console.log('No argument');
} else if (args.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
