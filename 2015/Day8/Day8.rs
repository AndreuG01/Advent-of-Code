fn input_path() -> String {
    std::env::args().nth(1).unwrap()
}

fn read_text() -> String {
    std::fs::read_to_string(input_path()).unwrap().trim_end().to_string()
}

fn memory_length(line: &str) -> usize {
    let inner = &line.as_bytes()[1..line.len() - 1]; // drop the surrounding quotes
    let mut i = 0;
    let mut mem_len = 0;
    while i < inner.len() {
        if inner[i] == b'\\' {
            i += if inner[i + 1] == b'x' { 4 } else { 2 };
        } else {
            i += 1;
        }
        mem_len += 1;
    }
    mem_len
}

fn main() {
    let file_content = read_text();

    let mut part_1_res = 0;
    let mut part_2_res = 0;

    for line in file_content.lines() {
        part_1_res += line.len() - memory_length(line);
        // Encoding adds the 2 new quotes and one backslash for each " and backslash
        part_2_res += 2 + line.chars().filter(|c| *c == '"' || *c == '\\').count();
    }

    println!("Part 1 res: {}", part_1_res);
    println!("Part 2 res: {}", part_2_res);
}
