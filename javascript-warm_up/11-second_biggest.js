#!/usr/bin/node
const size = [];
let result;

for (let i = 3; i < size; i++) {
    result = Number(process.argv[i]);
    size = size + size[result]
    if (size[i] > size[i - 1])[
        console.log(size[i])
    ]
  }
