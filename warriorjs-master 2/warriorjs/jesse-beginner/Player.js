class Player {
  playTurn(warrior) {
      warrior.feel('left');
      warrior.feel('right');
      if (warrior.feel('forward').isUnit()) {
        warrior.attack();
      } else {warrior.walk('forward')}
      }
    }
