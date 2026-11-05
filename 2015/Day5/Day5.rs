use std::collections::HashMap;

fn input_path() -> String {
    std::env::args().nth(1).unwrap()
}

fn read_text() -> String {
    std::fs::read_to_string(input_path()).unwrap().trim_end().to_string()
}

fn three_vowels(string: &str) -> bool {
    string.chars().filter(|c| "aeiou".contains(*c)).count() >= 3
}

fn repeated_chars(string: &str) -> bool {
    let chars = string.as_bytes();
    (1..chars.len()).any(|i| chars[i] == chars[i - 1])
}

fn substrings(string: &str) -> bool {
    !["ab", "cd", "pq", "xy"].iter().any(|sub| string.contains(sub))
}

fn two_grams(string: &str) -> bool {
    let mut first_seen = HashMap::new();
    for i in 0..string.len() - 1 {
        let pair = &string[i..i + 2];
        if let Some(first) = first_seen.get(pair) {
            if i - first >= 2 {
                return true;
            }
        }
        first_seen.entry(pair).or_insert(i);
    }
    false
}

fn three_grams(string: &str) -> bool {
    let chars = string.as_bytes();
    (0..chars.len() - 2).any(|i| chars[i] == chars[i + 2])
}

fn main() {
    let file_content = read_text();

    let mut part_1_res = 0;
    let mut part_2_res = 0;

    for string in file_content.lines() {
        if three_vowels(string) && repeated_chars(string) && substrings(string) {
            part_1_res += 1;
        }
        if two_grams(string) && three_grams(string) {
            part_2_res += 1;
        }
    }

    println!("Part 1 res: {}", part_1_res);
    println!("Part 2 res: {}", part_2_res);
}
