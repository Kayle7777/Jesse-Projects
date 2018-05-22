

class Player {
  import {Thoughts} from './thoughts'
  constructor() {
    this.health = 20;
  }

  isInjured(Player) {
    if (this.health < 20) {
      return "I am injured"
    } else {return "I am fine"}
  }
// it seems .think is a way to execute functions about stuff
  playTurn(warrior) {
    let healthStatus = warrior.think(this.isInjured())
    if (healthStatus = "I am fine") {}
  }

}
