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
    let mut part_2_done = false;

    for (i, c) in file_content.chars().enumerate() {
        if c == '(' {
            part_1_res += 1;
        } else {
            part_1_res -= 1;
        }
        if part_1_res == -1 && !part_2_done {
            part_2_res = i + 1;
            part_2_done = true;
        }
    }

    println!("Part 1 res: {}", part_1_res);
    println!("Part 2 res: {}", part_2_res);
}
