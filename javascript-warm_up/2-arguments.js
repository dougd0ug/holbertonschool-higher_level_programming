#!/usr/bin/node
const args = process.argv.length;

if (args.length === 2) {
  console.log('No argument');
}
if (args.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
