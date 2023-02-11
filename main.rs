fn meaningless_function(n: i32) -> i32 {
    let mut result = 0;
    for i in 0..n {
        result += i;
    }
    result
}

fn main() {
    println!("{}", meaningless_function(5));
}
