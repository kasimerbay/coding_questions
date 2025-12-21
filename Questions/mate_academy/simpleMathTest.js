function isPositive(number){
  return number > 0 ? true:false;
}

function isEven(number){
  return number%2 === 0 ? true:false;
}

function isDivisible10(number){
  return number%10 === 0 ? true:false;
}

function checkNumber(number) {
  return [isPositive(number),isEven(number),isDivisible10(number)];
}
