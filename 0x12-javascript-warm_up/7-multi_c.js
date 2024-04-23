#!/usr/bin/node
const [,, arg] = process.argv;
const num = parseInt(arg);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  let i = 1;
  while (i <= num) {
    console.log('C is fun');
    i++;
  }
}
