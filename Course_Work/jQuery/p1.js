 $('h1').click(function(){
  $(this).text('clicked!');
})


var head = $('h1');
head.css('color', 'red');
var newCSS = {
  'color': 'white',
  'background-color': 'red'
}
head.css(newCSS);
$('input').eq(1).attr('type', 'checkbox');

$('input').eq(0).keypress(function(event){
  $('h2').toggleClass('turnBlue');
  if (event.which === 13) {
    $('h2').toggleClass('turnRed');
  }
})

head.on('dblclick', function(){
  $(this).toggleClass('turnBlue');
})
$('input').eq(1).on('click', function(){
  $('.container').fadeOut(1000);
})
