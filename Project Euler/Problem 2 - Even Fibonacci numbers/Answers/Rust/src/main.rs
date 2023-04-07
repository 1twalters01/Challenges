use std::io::{self, Write};

fn main() {
    let mut input = String::new();
    print!("Enter the value of the upper bound: ");
    let _ = io::stdout().flush();
    io::stdin().read_line(&mut input).expect("Error reading from STDIN");
    let input:u64 = input.trim_end().parse().expect("Invalid number");

    let res: u64 = fib(input);
    summation: u64 = 0;
    for (value in res) {
        if (value % 2 == 0) {
            summation += value;
        }
    }
    println!("{}", res);
}

fn fib(limit: 