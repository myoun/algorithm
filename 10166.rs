use std::io;
fn gcd(a:i32, b:i32)->i32{
    while (a != b) {
        if (a > b) {
            return gcd(a - b, b);
        }
        else {
            return gcd(a, b - a);
        }
    }
    return a;
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed!");
    let split_string: Vec<&str> = input.split_whitespace().collect();
    let d1s = split_string[0];
    let d2s = split_string[1];
    let D1: i32 = d1s.parse().unwrap();
    let D2: i32 = d2s.parse().unwrap();
    
    let mut arr: [[bool;2001];2001] = [[false;2001];2001];

    let mut att = 0;
    
    for i in D1..(D2+1) {
        for j in 1..(i+1) {
            let g = gcd(i,j);
            
            if (arr[i][j] == ) {
                vec.push(d);
            }
        }
    }
    println!("{}", vec.len());
}