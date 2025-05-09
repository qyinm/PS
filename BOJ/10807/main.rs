use std::io;

fn main() {
    // 정수의 개수 입력 받기
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let _n: usize = input.trim().parse().unwrap();
    
    // n개의 정수 입력 받기
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let numbers: Vec<i32> = input
        .trim()
        .split_whitespace()
        .map(|s| s.parse().unwrap())
        .collect();
    
    // 찾을 정수 입력 받기
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let v: i32 = input.trim().parse().unwrap();
    
    let count = numbers.iter().filter(|&&num| num == v).count();
    
    println!("{}", count);
}
