var userInput = 'rock'

function computerChoice() {
  var randomNumber = Math.floor(Math.random() * 3)
  switch(randomNumber) {
    case 0:
    return 'rock'
    case 1:
    return 'paper'
    case 2:
    return 'scissors'
    break;
  }
}

var computerChoice = computerChoice()

function determineWinner(userInput, computerChoice) {
  
  if(userInput === computerChoice) {
    return console.log('The game is a tie!');
  }

  if(userInput === 'rock') {
    if(computerChoice === 'scissors') {
      console.log('You win! Your rock crushes scissors!');
    }
    else {console.log('You lose! Your rock was covered by paper!');}
  }
  
  if(userInput === 'paper') {
    if(computerChoice === 'rock') {
      console.log('You win! Your paper covers rock!');
    }
    else {console.log('You lose! Your paper was cut by scissors!');}
  }
  if(userInput === 'scissors') {
    if(computerChoice === 'paper') {
      console.log('You win! Your scissors cuts paper!');
    }
    else {console.log('You lose! Your scissors was crushed by rock!');}
    }
  
  }

function playGame() {
  console.log(determineWinner());
}

playGame()