fn input_path() -> String {
    std::env::args().nth(1).unwrap()
}

fn read_text() -> String {
    std::fs::read_to_string(input_path()).unwrap().trim_end().to_string()
}

fn main() {
    let target: usize = read_text().parse().unwrap();

    // House n gets 10 presents from each elf that divides n, and house target / 10 + 1
    // alone gets at least target presents from its own elf, so the answer can't be further away
    let limit = target / 10 + 1;
    let mut houses = vec![0; limit + 1];
    for elf in 1..=limit {
        for house in (elf..=limit).step_by(elf) {
            houses[house] += elf * 10;
        }
    }
    let part_1_res = (1..=limit).find(|house| houses[*house] >= target).unwrap();

    // Part 2: each elf only visits 50 houses, but leaves 11 presents per house
    let limit = target / 11 + 1;
    let mut houses = vec![0; limit + 1];
    for elf in 1..=limit {
        for house in (elf..=limit.min(elf * 50)).step_by(elf) {
            houses[house] += elf * 11;
        }
    }
    let part_2_res = (1..=limit).find(|house| houses[*house] >= target).unwrap();

    println!("Part 1 res: {}", part_1_res);
    println!("Part 2 res: {}", part_2_res);
}
