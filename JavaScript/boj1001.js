let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split(' ');

let [a, b] = input.map(Number);

if(a > b) {
    console.log('>');
} else if(a == b) {
    console.log('==');
} else{
    console.log('<');
}
console.log(a == b)