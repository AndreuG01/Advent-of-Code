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

    for line in file_content.lines() {
        let elem: Vec<i64> = line.split('x').map(|num| num.parse().unwrap()).collect();
        let (l, w, h) = (elem[0], elem[1], elem[2]);

        let a_side_1 = l * w;
        let a_side_2 = w * h;
        let a_side_3 = h * l;

        let p_side_1 = 2 * l + 2 * w;
        let p_side_2 = 2 * w + 2 * h;
        let p_side_3 = 2 * h + 2 * l;

        part_1_res += 2 * a_side_1 + 2 * a_side_2 + 2 * a_side_3 + a_side_1.min(a_side_2).min(a_side_3);
        part_2_res += p_side_1.min(p_side_2).min(p_side_3) + l * w * h;
    }

    println!("Part 1 res: {}", part_1_res);
    println!("Part 2 res: {}", part_2_res);
}
