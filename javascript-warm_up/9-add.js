#!/usr/bin/node

function add (a, b) {
  console.log(a + b);
}

const firstArg = Number(process.argv[2]);
const secondArg = Number(process.argv[3]);

add(firstArg, secondArg);
