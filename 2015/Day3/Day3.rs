use std::collections::HashSet;

fn input_path() -> String {
    std::env::args().nth(1).unwrap()
}

fn read_text() -> String {
    std::fs::read_to_string(input_path()).unwrap().trim_end().to_string()
}

fn move_position(position: (i32, i32), elem: char) -> (i32, i32) {
    match elem {
        '^' => (position.0, position.1 + 1),
        '>' => (position.0 + 1, position.1),
        '<' => (position.0 - 1, position.1),
        _ => (position.0, position.1 - 1),
    }
}

fn main() {
    let file_content = read_text();

    let mut curr_pos = (0, 0);
    let mut unique_pos = HashSet::from([curr_pos]);
    for elem in file_content.chars() {
        curr_pos = move_position(curr_pos, elem);
        unique_pos.insert(curr_pos);
    }
    let part_1_res = unique_pos.len();

    let mut santas = [(0, 0), (0, 0)]; // Santa and Robo-Santa
    let mut visited = HashSet::from([(0, 0)]);
    for (i, elem) in file_content.chars().enumerate() {
        santas[i % 2] = move_position(santas[i % 2], elem);
        visited.insert(santas[i % 2]);
    }
    let part_2_res = visited.len();

    println!("Part 1 res: {}", part_1_res);
    println!("Part 2 res: {}", part_2_res);
}
