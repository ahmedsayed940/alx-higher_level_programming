#!/usr/bin/node
const [,, arg1, arg2] = process.argv;
if (!arg1) {
  console.log('No argument');
} else if (arg1 && !arg2) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
