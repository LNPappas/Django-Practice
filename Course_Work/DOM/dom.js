var header = document.querySelector("h1")

header.style.color = 'red'

function getRandomColor(){
  var letters = "0123456789ABCDEF";
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random()*16)];
  }
  return color
}

function changeHeaderColor(){
  colorInput = getRandomColor()
  header.style.color = colorInput;
}

setInterval("changeHeaderColor()",500);

var p = document.querySelector("p");
p.textContent = 'New TEXT!!!';

var p2 = document.querySelector("#p2");
p2.innerHTML = "<strong>I'm Bold!!!</strong>";

var sp = document.querySelector("#special");
var link = sp.querySelector("a");
link.setAttribute("href", "https://www.amazon.com");

function changeColor() {
  colorC = getRandomColor()
  link.style.color = colorC;
}
//Events: click, hover, double click, drag, etc...
link.addEventListener("click", changeColor());

var hTwo = document.querySelector("#two");
var t = hTwo.textContent;
hTwo.addEventListener("mouseover",function(){
  hTwo.textContent = "Hovering!!!";
  hTwo.style.color = getRandomColor();
});

hTwo.addEventListener("mouseout",function(){
  hTwo.textContent = t;
  hTwo.style.color = 'black';
});
