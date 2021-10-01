const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const caseNum = Number(input[0]);

for(let i = 1; i <= caseNum; i++){
    let data = input[i].split(' ').map(Number);
    let len = data[0];
    data = data.slice(1);
    let sum = data.reduce((x, y) => x + y);
    let cnt = 0;
    let average = sum / len;
    for (let j = 0; j < len; j++){
        if(data[j] > average){
            cnt++;
        }
    }
    let result = (cnt / len * 100).toFixed(3);
    console.log(result + '%');
}