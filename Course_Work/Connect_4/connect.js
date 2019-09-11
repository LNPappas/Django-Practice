var bluePlayer = 'BLUE';
var blueColor = 'rgb(0, 145, 255)';
var redPlayer = 'RED';
var redColor = 'rgb(222, 80, 80)';
var background = 'rgb(40, 46, 48)';

var table = $('table tr')
var board = $('.board button');
var head = $('h1');
var btn = $('#b');

head.css('color', 'rgb(71, 231, 255)')

function changeColor(row, col, color){
  return table.eq(row).find('td').eq(col).find('button').css('background-color', color)
}

function getColor(row, col){
  return table.eq(row).find('td').eq(col).find('button').css('background-color')
}

function lowestRow(col, currentColor) {
  for (var i = 5; i > -1 ; i--) {
    var color = getColor(i, col);
    if (color === background) {
      return changeColor(i, col, currentColor);
    }
  }
  return background;
}


function colorCheck(one,two,three,four){
    return (one===two && one===three && one===four && one !== background && one !== undefined);
  }

function checkWin() {
  return horizontal() || vertical() || diagonal();
}

function horizontal() {
  for (var row = 0; row < 6; row++) {
    for (var col = 0; col < 4; col++) {
      var win = colorCheck(getColor(row,col), getColor(row,col+1),
          getColor(row,col+2), getColor(row,col+3))
      if (win === true) {
        setWinner(row,col,row,col+1,row,col+2,row,col+3)
        return true
      }
    }
  }
}

function vertical() {
  for (var col = 0; col < 7; col++) {
    for (var row = 0; row < 3; row++) {
      var win = colorCheck(getColor(row,col), getColor(row+1,col),
          getColor(row+2,col), getColor(row+3,col))
      if (win === true) {
        setWinner(row,col,row+1,col,row+2,col,row+3,col)
        return true
      }
    }
  }
}
function diagonal() {
  for (var col = 0; col < 5; col++) {
    for (var row = 0; row < 7; row++) {
      var win = colorCheck(getColor(row,col), getColor(row+1,col+1),
          getColor(row+2,col+2), getColor(row+3,col+3))
      if (win === true) {
        setWinner(row,col,row+1,col+1,row+2,col+2,row+3,col+3)
        return true
      } else if (colorCheck(getColor(row,col), getColor(row-1,col+1),
          getColor(row-2,col+2), getColor(row-3,col+3)) ===true) {
          setWinner(row,col,row+1,col-1,row-2,col-2,row-3,col+3)
        return true
      }
    }
  }
}
function setWinner(row1, col1, row2, col2, row3, col3, row4, col4) {
  console.log("setting winner...");
  for (var col = 0; col < 7; col++) {
    for (var row = 0; row < 9; row++) {
      table.eq(row).find('td').eq(col).find('button').css('background-color', background);
      console.log(currentColor);
    }
  }
  table.eq(row1).find('td').eq(col1).find('button').css('background-color', currentColor);
  table.eq(row2).find('td').eq(col2).find('button').css('background-color', currentColor);
  table.eq(row3).find('td').eq(col3).find('button').css('background-color', currentColor);
  table.eq(row4).find('td').eq(col4).find('button').css('background-color', currentColor);
  return true
}

function endGame(name, color) {
  head.text(name+" WINS!!!!").css('color', color);
}

btn.on('click', function(){
  btn.text('RESTART');
  currentColor = blueColor;
  currentPlayer = bluePlayer;
  head.text(currentPlayer+"\'S TURN: ").css('color', currentColor);

  board.on('click', function(){
    var col = $(this).closest("td").index();
    var check = lowestRow(col, currentColor);
    if (check === background) {
      alert("Column is full, try another.")
    } else {
      var win = checkWin();
      if (win === true) {
        endGame(currentPlayer, currentColor);
      } else {
        if (currentPlayer === bluePlayer) {
          currentPlayer = redPlayer;
          currentColor = redColor;
          head.text(currentPlayer+"\'S TURN: ").css('color', currentColor);

        } else {
          currentPlayer = bluePlayer;
          currentColor = blueColor;
          head.text(currentPlayer+"\'S TURN: ").css('color', currentColor);
        }
      }
    }
  });

  btn.on('click',function(){
    document.location.reload(true);
  })
});
