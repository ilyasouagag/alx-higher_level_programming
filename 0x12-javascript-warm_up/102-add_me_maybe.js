#!/usr/bin/node
exports.addMaybe = function (number, theFunction) {
  number++;
  theFunction(number);
};
