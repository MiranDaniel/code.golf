fn main(){for n in 1..101{if n%(n.to_string().chars().map(|c|c as i32-48).sum::<i32>())<1{println!("{n}")}}}