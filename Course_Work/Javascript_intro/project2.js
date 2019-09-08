var num = prompt("What is the weight in pounds:")
alert(num + " pounds is: " + num*0.454 + " kilograms")
console.log("Converstion Completed")

if (num > 50){
  console.log("lbs Greater than 50");
}
else{
  console.log("lbs < 50");
}

for (var i = 0; i < 5; i++) {
  console.log(i);
}

word = 'abcdefghijk'
for (var i = 0; i < word.length; i=i+2) {
  console.log(word[i]);
}
