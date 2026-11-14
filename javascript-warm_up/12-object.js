#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
// const stops reassigning the variable, but object properties can still change
myObject.value = 89;
console.log(myObject);
