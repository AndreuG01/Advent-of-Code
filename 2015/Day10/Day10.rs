fn input_path() -> String {
    std::env::args().nth(1).unwrap()
}

fn read_text() -> String {
    std::fs::read_to_string(input_path()).unwrap().trim_end().to_string()
}

fn look_and_say(s: &str) -> String {
    let chars = s.as_bytes();
    let mut count = 1;
    let mut val = chars[0] as char;
    let mut new_str = String::new();
    for i in 1..chars.len() {
        if chars[i] as char == val {
            count += 1;
        } else {
            new_str.push_str(&count.to_string());
            new_str.push(val);
            count = 1;
        }
        val = chars[i] as char;
    }
    new_str.push_str(&count.to_string());
    new_str.push(val);
    new_str
}

fn main() {
    let mut seq = read_text();

    let mut part_1_res = 0;

    for i in 0..50 {
        seq = look_and_say(&seq);
        if i == 39 {
            part_1_res = seq.len();
        }
    }
    let part_2_res = seq.len();

    println!("Part 1 res: {}", part_1_res);
    println!("Part 2 res: {}", part_2_res);
}
