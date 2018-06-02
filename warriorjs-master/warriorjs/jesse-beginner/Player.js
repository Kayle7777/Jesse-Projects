class Player {
  constructor() {
    this.health = 20;
    this.names = [];
  }

  vector(x,y) {
    let directions = [];

    for (var i = 0; i < x.length; i++) {
      directions[i] = y.feel(x[i]);}
    for (var i = 0; i <x.length; i++) {
      directions[i].name = x[i];}

    return directions
  }

  isInjured(Player) {
    if (this.health < 20) {
      return "I am injured."
    } else {return "I am not injured."}
  }
// it seems .think is a way to console.log stuff
  playTurn(warrior) {
    let healthStatus = warrior.think(this.isInjured());
//    if (healthStatus = "I am fine") {
    let x = this.vector(['forward', 'right', 'backward', 'left'], warrior);

    // try thinking Object.keys(x) to list object properties
    // x properties getLocation,getUnit,isEmpty,isStairs,isUnit,isWall
    // x is now a list of objects
    // warrior.think('I am thinking ' + Object.keys(x[0]))

    for (var i = 0; i < x.length; i++) {this.names.push(x[i].name)}
    warrior.think(this.names[0])

    }




    // warrior.think("Now I'm going to think if " + this.names + " are empty...")
    // for (var i = 0; i < x.length; i++){
    //   warrior.think(x[i].name + ' is ' + x[i].isEmpty() + ".")}
    }
