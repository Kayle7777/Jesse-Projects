function randInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}

let a = ['World','Linus','Osei','Greg','Jesse','David','Daniel','Blake']

console.log('Hello' + " " + a[randInt(a.length)] + "!")
