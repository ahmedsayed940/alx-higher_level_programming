#!/usr/bin/node
function secondBI (numbers) {
  if (numbers.length <= 1) {
    return 0;
  }

  let max = parseInt(numbers[0]);
  let secondMax = parseInt(numbers[1]);

  if (max < secondMax) {
    [max, secondMax] = [secondMax, max];
  }

  for (let i = 2; i < numbers.length; i++) {
    const num = parseInt(numbers[i]);
    if (num > max) {
      secondMax = max;
      max = num;
    } else if (num > secondMax && num !== max) {
      secondMax = num;
    }
  }

  return secondMax;
}

const args = process.argv.slice(2);
console.log(secondBI(args));
