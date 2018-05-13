// let fs = require("fs"),
//     path = require("path"),
//     filePath = path.join(__dirname, 'index.html')

// I originally thought coding via node would be easier, because I learned python by using the terminal. Will continue to try.
//fs.readFile(filePath, {encoding: 'utf-8'}, function(err,data){
//  if (!err) {
//    console.log('received data: ' + data);
//  }
//  else {
//    console.log(err);
//  }
//})

function reDiv(id, ud) {
  let div = document.getElementById(id);
  // To parse the string "150px" into the int 150
  let h = parseInt(div.style.height)+ud;
  div.style.height = h + "px";
  div.style.width = h + "px";

}

function color(id) {
  let div = document.getElementById(id);
  div.style.backgroundColor = 'blue';
}

function fade(id, ud) {
  let div = document.getElementById(id);
  div.style.opacity = div.style.opacity - ud
}

function reset() {
  let div = document.getElementById('box')
  div.style.backgroundColor = 'orange';
  div.style.height = '150px';
  div.style.width = '150px';
  div.style.opacity = '1.0';
}
