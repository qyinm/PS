const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
let data = [];
rl.on("line", function(line){
    data.push(parseInt(line))
}).on("close", function(){
    const [x, y] = [data[0], data[1]]
    
    if(x > 0 && y > 0){
        console.log(1);
    }else if(x < 0 && y > 0){
        console.log(2);
    }else if(x < 0 && y < 0){
        console.log(3);
    }else{
        console.log(4);
    }
    process.exit();
})
