#!/usr/bin/node
/* Function that increments and calls a function */
exports.addMeMaybe = function (number, theFunction) {
  const num = number + 1;
  theFunction(num);
};
