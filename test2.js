var userInput = 'Rock'
userInput = userInput.toLowerCase();

function computerChoice() {
  var randomNumber = Math.floor(Math.random() * 3)
	switch(randomNumber) {
  	 case 0:
    	 return 'rock';
   	case 1:
    	 return 'paper';
   	case 2:
    	 return 'scissors';
       break;
    }
  }

var userChoice = userInput

function determineWinner(userChoice, computerChoice()) {
var computerChoice = computerChoice()
  if (userChoice === computerChoice) {
    return console.log('The game was a tie.')
  }

  if (userChoice === 'rock' && computerChoice === 'scissors') {
    return console.log('You win! Rock crushes scissors!');
  }
    else {
      return console.log('The computer wins! Paper covers rock!');
    }

  if (userChoice === 'scissors' && computerChoice === 'paper') {
    return console.log('You win! Scissors cuts paper!');
  }
    else {
      return console.log('The computer wins! Rock crushes scissors!');
    }


  if (userChoice === 'paper' && computerChoice === 'rock') {
    return console.log('You win! Paper covers rock!');
  }
    else {
      return console.log('The computer wins! Scissors cuts paper!');
    }

}

function playGame() {
  console.log(userChoice, computerChoice());
  console.log(determineWinner();
}
