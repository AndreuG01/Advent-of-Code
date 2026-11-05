use std::collections::HashSet;
use std::time::{SystemTime, UNIX_EPOCH};

fn input_path() -> String {
    std::env::args().nth(1).unwrap()
}

fn read_text() -> String {
    std::fs::read_to_string(input_path()).unwrap().trim_end().to_string()
}

// Rust has no random numbers in its standard library: a small xorshift is enough to shuffle
fn shuffle(rules: &mut Vec<(String, String)>, seed: &mut u64) {
    for i in (1..rules.len()).rev() {
        *seed ^= *seed << 13;
        *seed ^= *seed >> 7;
        *seed ^= *seed << 17;
        rules.swap(i, (*seed % (i as u64 + 1)) as usize);
    }
}

fn fewest_steps(molecule: &str, replacements: &[(String, String)]) -> i32 {
    // Work backwards from the molecule to "e". Every way down takes the same number
    // of steps, but a greedy path can get stuck, so restart with a new order if it does
    let mut rules = replacements.to_vec();
    let mut seed = SystemTime::now().duration_since(UNIX_EPOCH).unwrap().as_nanos() as u64 | 1;
    loop {
        shuffle(&mut rules, &mut seed);
        let mut curr = molecule.to_string();
        let mut steps = 0;
        let mut changed = true;
        while curr != "e" && changed {
            changed = false;
            for (source, target) in &rules {
                if curr.contains(target.as_str()) {
                    curr = curr.replacen(target.as_str(), source, 1);
                    steps += 1;
                    changed = true;
                    break;
                }
            }
        }
        if curr == "e" {
            return steps;
        }
    }
}

fn main() {
    let file_content = read_text();

    let (rules, molecule) = file_content.split_once("\n\n").unwrap();
    let replacements: Vec<(String, String)> = rules
        .lines()
        .map(|line| {
            let (source, target) = line.split_once(" => ").unwrap();
            (source.to_string(), target.to_string())
        })
        .collect();

    let mut molecules = HashSet::new();
    for (source, target) in &replacements {
        for (i, _) in molecule.match_indices(source.as_str()) {
            molecules.insert(format!("{}{}{}", &molecule[..i], target, &molecule[i + source.len()..]));
        }
    }

    let part_1_res = molecules.len();
    let part_2_res = fewest_steps(molecule, &replacements);

    println!("Part 1 res: {}", part_1_res);
    println!("Part 2 res: {}", part_2_res);
}
