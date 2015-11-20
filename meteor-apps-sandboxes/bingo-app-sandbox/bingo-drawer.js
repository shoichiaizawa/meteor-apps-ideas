var numbers = new Array();

for (var i = 1; i <= 75; i++)
  numbers.push(i);

console.log(numbers);

while (numbers.length > 0) {
  // Random Index position in the array
  var randIdx = Math.floor(Math.random() * numbers.length);

  console.log("Number drawn:", numbers[randIdx]);

  // Splice out a random element using the ri var
  var rs = numbers.splice(randIdx, 1);
}

console.log(""numbers);

