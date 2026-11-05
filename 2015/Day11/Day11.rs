fn input_path() -> String {
    std::env::args().nth(1).unwrap()
}

fn read_text() -> String {
    std::fs::read_to_string(input_path()).unwrap().trim_end().to_string()
}

fn increasing_straight(string: &[u8]) -> bool {
    (2..string.len()).any(|i| {
        let (a, b, c) = (string[i], string[i - 1], string[i - 2]);
        b == c + 1 && a == b + 1
    })
}

fn letters(string: &[u8]) -> bool {
    !string.iter().any(|c| [b'i', b'o', b'l'].contains(c))
}

fn two_grams(string: &[u8]) -> bool {
    let mut found = 0;
    let mut i = 1;
    while i < string.len() {
        if string[i] == string[i - 1] {
            found += 1;
            i += 2; // skip so the pairs can't overlap
        } else {
            i += 1;
        }
    }
    found >= 2
}

fn is_valid(string: &[u8]) -> bool {
    increasing_straight(string) && two_grams(string) && letters(string)
}

fn increment(string: &mut Vec<u8>) {
    for i in (0..string.len()).rev() {
        if string[i] == b'z' {
            string[i] = b'a'; // wrap around and carry to the next letter on the left
        } else {
            string[i] += 1;
            break;
        }
    }
}

fn next_password(string: &[u8]) -> Vec<u8> {
    let mut next = string.to_vec();
    increment(&mut next);
    while !is_valid(&next) {
        increment(&mut next);
    }
    next
}

fn main() {
    let file_content = read_text();

    let part_1 = next_password(file_content.as_bytes());
    let part_2 = next_password(&part_1);

    let part_1_res = String::from_utf8(part_1).unwrap();
    let part_2_res = String::from_utf8(part_2).unwrap();

    println!("Part 1 res: {}", part_1_res);
    println!("Part 2 res: {}", part_2_res);
}
