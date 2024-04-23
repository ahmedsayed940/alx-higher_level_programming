#!/usr/bin/node
const [,, arg] = process.argv;
const num = parseInt(arg);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < num) {
    let row = '';
    for (let j = 0; j < num; j++) {
      row += 'X';
    }
    console.log(row);
    i++;
  }
}
