use std::collections::HashMap;

fn input_path() -> String {
    std::env::args().nth(1).unwrap()
}

fn read_text() -> String {
    std::fs::read_to_string(input_path()).unwrap().trim_end().to_string()
}

fn run(instructions: &[Vec<String>], a: i64, b: i64) -> HashMap<String, i64> {
    let mut registers = HashMap::from([("a".to_string(), a), ("b".to_string(), b)]);
    let mut pc = 0i32;
    while pc >= 0 && (pc as usize) < instructions.len() {
        let instruction = &instructions[pc as usize];
        let target = &instruction[1];
        match instruction[0].as_str() {
            "hlf" => *registers.get_mut(target).unwrap() /= 2,
            "tpl" => *registers.get_mut(target).unwrap() *= 3,
            "inc" => *registers.get_mut(target).unwrap() += 1,
            "jmp" => {
                pc += target.parse::<i32>().unwrap();
                continue;
            }
            "jie" if registers[target] % 2 == 0 => {
                pc += instruction[2].parse::<i32>().unwrap();
                continue;
            }
            // jump if ONE, not if odd
            "jio" if registers[target] == 1 => {
                pc += instruction[2].parse::<i32>().unwrap();
                continue;
            }
            _ => {}
        }
        pc += 1;
    }
    registers
}

fn main() {
    let file_content = read_text();

    let instructions: Vec<Vec<String>> = file_content
        .lines()
        .map(|line| line.replace(',', "").split(' ').map(String::from).collect())
        .collect();

    let registers = run(&instructions, 0, 0);
    // The puzzle's example asks for register a
    let part_1_res = if input_path().contains("example") { registers["a"] } else { registers["b"] };

    // Part 2: same program, but register a starts at 1
    let part_2_res = run(&instructions, 1, 0)["b"];

    println!("Part 1 res: {}", part_1_res);
    println!("Part 2 res: {}", part_2_res);
}
