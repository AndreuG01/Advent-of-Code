fn input_path() -> String {
    std::env::args().nth(1).unwrap()
}

fn read_text() -> String {
    std::fs::read_to_string(input_path()).unwrap().trim_end().to_string()
}

fn main() {
    let file_content = read_text();

    let mut points = vec![vec![0i32; 1000]; 1000];
    let mut points_2 = vec![vec![0i32; 1000]; 1000];

    for line in file_content.lines() {
        let elems: Vec<&str> = line.split(' ').collect();
        // "toggle a,b through c,d" has 4 words, "turn on a,b through c,d" has 5
        let action = if elems.len() == 4 { "toggle" } else { elems[1] };
        let nums_f: Vec<usize> = elems[elems.len() - 3].split(',').map(|num| num.parse().unwrap()).collect();
        let nums_t: Vec<usize> = elems[elems.len() - 1].split(',').map(|num| num.parse().unwrap()).collect();

        for x in nums_f[0]..=nums_t[0] {
            for y in nums_f[1]..=nums_t[1] {
                match action {
                    "off" => {
                        points[x][y] = 0;
                        points_2[x][y] = (points_2[x][y] - 1).max(0);
                    }
                    "on" => {
                        points[x][y] = 1;
                        points_2[x][y] += 1;
                    }
                    _ => {
                        points[x][y] = 1 - points[x][y];
                        points_2[x][y] += 2;
                    }
                }
            }
        }
    }

    let part_1_res: i32 = points.iter().flatten().sum();
    let part_2_res: i32 = points_2.iter().flatten().sum();

    println!("Part 1 res: {}", part_1_res);
    println!("Part 2 res: {}", part_2_res);
}
