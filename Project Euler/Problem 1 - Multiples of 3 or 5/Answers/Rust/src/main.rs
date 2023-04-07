use std::io::{self, Write};

fn main() {
    let mut input = String::new();
    print!("Enter a number: ");
    let _ = io::stdout().flush();
    io::stdin().read_line(&mut input).expect("Error reading from STDIN");
    let input:u64 = input.trim_end().parse().expect("Invalid number");
    let res:u64 = multiples_of_3_and_5(input);
    println!("{}", res);
}

fn multiples_of_3_and_5(input:u64) -> u64 {
    let limit:u64 = input -1;
    let limits = limits_for_3_5_and_15(limit);
    let (summation3, summation5, summation15) = summations_for_3_5_and_15(limits.0, limits.1, limits.2);
    let answer:u64 = summation3 + summation5 - summation15;
    return answer;
}

fn limits_for_3_5_and_15(limit:u64) -> (u64, u64, u64) {
    let (limit3, limit5, limit15) = (limit/3, limit/5, limit/15);
    return (limit3, limit5, limit15);
}

fn summations_for_3_5_and_15(limit3:u64, limit5:u64, limit15:u64) -> (u64, u64, u64) {
    let summation3:u64 = (limit3.pow(2) + limit3)*3/2;
    let summation5:u64 = (limit5.pow(2) + limit5)*5/2;
    let summation15:u64 = (limit15.pow(2) + limit15)*15/2;
    return (summation3, summation5, summation15);
}