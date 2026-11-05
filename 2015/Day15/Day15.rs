fn input_path() -> String {
    std::env::args().nth(1).unwrap()
}

fn read_text() -> String {
    std::fs::read_to_string(input_path()).unwrap().trim_end().to_string()
}

fn combinations_sum(num_elems: usize, total: i64, amounts: &mut Vec<i64>, visit: &mut dyn FnMut(&[i64])) {
    if num_elems == 1 {
        // The last value has to be whatever is left
        amounts.push(total);
        visit(amounts);
        amounts.pop();
        return;
    }
    for first in 0..=total {
        amounts.push(first);
        combinations_sum(num_elems - 1, total - first, amounts, visit);
        amounts.pop();
    }
}

fn dot(prop: &[i64], amounts: &[i64]) -> i64 {
    prop.iter().zip(amounts).map(|(a, b)| a * b).sum()
}

fn main() {
    let file_content = read_text();

    let mut multipliers: Vec<Vec<i64>> = vec![vec![]; 4];
    let mut calories = vec![];

    for line in file_content.lines() {
        let line = line.replace(',', "");
        let splited_elems: Vec<&str> = line.split(' ').collect();
        for (i, position) in [2, 4, 6, 8].iter().enumerate() {
            multipliers[i].push(splited_elems[*position].parse().unwrap());
        }
        calories.push(splited_elems[10].parse::<i64>().unwrap());
    }

    let mut part_1_res = 0;
    let mut part_2_res = 0;

    let num_elems = calories.len();
    combinations_sum(num_elems, 100, &mut vec![], &mut |amounts| {
        let curr_res: i64 = multipliers.iter().map(|prop| dot(prop, amounts).max(0)).product();
        part_1_res = part_1_res.max(curr_res);
        // Part 2: only cookies with exactly 500 calories
        if dot(&calories, amounts) == 500 {
            part_2_res = part_2_res.max(curr_res);
        }
    });

    println!("Part 1 res: {}", part_1_res);
    println!("Part 2 res: {}", part_2_res);
}
