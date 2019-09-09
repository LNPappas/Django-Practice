var data =  $('h1')

data.click(function(){
  console.log('click!');
})


var head = $('h1');
head.css('color', 'red');
var newCSS = {
  'color': 'white',
  'background-color': 'red'
}
head.css(newCSS);
$('input').eq(1).attr('type', 'checkbox');
