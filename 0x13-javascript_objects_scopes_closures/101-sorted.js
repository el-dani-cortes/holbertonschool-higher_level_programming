#!/usr/bin/node
const dic = require('./101-data').dict;
const newDic = {};
for (const key in dic) {
  const value = dic[key];
  if (Object.prototype.hasOwnProperty.call(newDic, value)) {
    const a = newDic[value];
    a.push(key);
    newDic[value] = a;
  } else {
    const array = [key];
    newDic[value] = array;
  }
}
console.log(newDic);
