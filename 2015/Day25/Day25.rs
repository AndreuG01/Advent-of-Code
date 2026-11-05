fn input_path() -> String {
    std::env::args().nth(1).unwrap()
}

fn read_text() -> String {
    std::fs::read_to_string(input_path()).unwrap().trim_end().to_string()
}

fn main() {
    let file_content = read_text();

    let nums: Vec<u64> = file_content
        .split(|c: char| !c.is_ascii_digit())
        .filter(|part| !part.is_empty())
        .map(|num| num.parse().unwrap())
        .collect();
    let (row, col) = (nums[0], nums[1]);

    // Codes fill the grid by diagonals: (row, col) is on diagonal row + col - 1,
    // and all the diagonals before it hold 1 + 2 + ... + (diagonal - 1) codes
    let diagonal = row + col - 1;
    let position = diagonal * (diagonal - 1) / 2 + col;

    let mut code: u64 = 20151125;
    for _ in 0..position - 1 {
        code = code * 252533 % 33554393;
    }

    let part_1_res = code;
    let part_2_res = 0;

    println!("Part 1 res: {}", part_1_res);
    println!("Part 2 res: {}", part_2_res);
}
