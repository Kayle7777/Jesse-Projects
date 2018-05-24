class Player {
  constructor() {
    this.health = 20;
  }

  thoughts(x,y) {
    for (var i = 0; i < x.length; i++) {
      return y.feel(x[i]);
    }
  }

  isInjured(Player) {
    if (this.health < 20) {
      return "I am injured"
    } else {return "I am fine"}
  }
// it seems .think is a way to execute functions about stuff
  playTurn(warrior) {
    let healthStatus = warrior.think(this.isInjured());
    if (healthStatus = "I am fine") {
      let x = this.thoughts(['forward', 'right', 'backward', 'left'], warrior);
      // try thinking Object.keys(x) to list object properties
      // x properties getLocation,getUnit,isEmpty,isStairs,isUnit,isWall
      warrior.think('I am thinking ' + x.isEmpty())
      }
    }
}

  // feeler(context) {
    // var defaults = {
    //   n: 'north',
    //   e: 'east',
    //   s: 'south',
    //   w: 'west'
    // };
    // var context = extend(defaults, context);
    // for (var i = 0; i < context.length; i++) {
    //   this.directions.push(Player.warrior.feel(x))
    // }
