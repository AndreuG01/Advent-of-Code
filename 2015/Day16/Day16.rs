use std::collections::HashMap;

fn input_path() -> String {
    std::env::args().nth(1).unwrap()
}

fn read_text() -> String {
    std::fs::read_to_string(input_path()).unwrap().trim_end().to_string()
}

fn main() {
    let file_content = read_text();

    let mut part_1_res = 0;
    let mut part_2_res = 0;

    let target = HashMap::from([
        ("children", 3),
        ("cats", 7),
        ("samoyeds", 2),
        ("pomeranians", 3),
        ("akitas", 0),
        ("vizslas", 0),
        ("goldfish", 5),
        ("trees", 3),
        ("cars", 2),
        ("perfumes", 1),
    ]);

    for (i, line) in file_content.lines().enumerate() {
        let line = line.replace(':', "").replace(',', "");
        let parts: Vec<&str> = line.split(' ').skip(2).collect();

        let mut matches = true;
        let mut matches_2 = true;
        for pair in parts.chunks(2) {
            let detect = pair[0];
            let val: i32 = pair[1].parse().unwrap();
            let expected = target[detect];
            if expected != val {
                matches = false;
            }

            // Part 2: cats and trees are lower bounds, pomeranians and goldfish upper bounds
            let ok = match detect {
                "cats" | "trees" => val > expected,
                "pomeranians" | "goldfish" => val < expected,
                _ => val == expected,
            };
            if !ok {
                matches_2 = false;
            }
        }
        if matches {
            part_1_res = i + 1;
        }
        if matches_2 {
            part_2_res = i + 1;
        }
    }

    println!("Part 1 res: {}", part_1_res);
    println!("Part 2 res: {}", part_2_res);
}
