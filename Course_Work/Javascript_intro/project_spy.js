first = prompt("What is your first name?");
last = prompt("What is your last name?");
age = prompt("How old are you?");
height = prompt("How tall are you in centimeters?");
pet = prompt("What is your pet's name?");
letter = pet[pet.length - 1]

if (first[0] === last[0]) {
  if (age > 20 || age < 30) {
    if (height >== 170) {
      if (letter === 'y') {
        console.log("SPY!!!");
      }
    }
  }

}
