fn input_path() -> String {
    std::env::args().nth(1).unwrap()
}

fn read_text() -> String {
    std::fs::read_to_string(input_path()).unwrap().trim_end().to_string()
}

fn main() {
    let file_content = read_text();

    let nums: Vec<i32> = file_content.split_whitespace().map(|elem| elem.parse().unwrap()).collect();

    let mut part_1_res = 0;
    let mut part_2_res = 0;

    let target = if input_path().contains("example") { 25 } else { 150 };

    // Each bit of mask says if a container is used, so same-size containers stay different.
    // ways[size] counts the matching groups with that many containers.
    let mut ways = vec![0; nums.len() + 1];
    for mask in 1u32..(1 << nums.len()) {
        let total: i32 = (0..nums.len()).filter(|i| mask & (1 << i) != 0).map(|i| nums[i]).sum();
        if total == target {
            ways[mask.count_ones() as usize] += 1;
        }
    }

    for curr_res in ways {
        part_1_res += curr_res;
        // Part 2: sizes go up, so the first size with a match is the minimum
        if part_2_res == 0 {
            part_2_res = curr_res;
        }
    }

    println!("Part 1 res: {}", part_1_res);
    println!("Part 2 res: {}", part_2_res);
}
