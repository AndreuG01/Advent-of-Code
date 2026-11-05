fn input_path() -> String {
    std::env::args().nth(1).unwrap()
}

fn read_text() -> String {
    std::fs::read_to_string(input_path()).unwrap().trim_end().to_string()
}

// Rust has no JSON in its standard library, so here is a small parser for what the input uses
enum Value {
    Number(i64),
    Text(String),
    Array(Vec<Value>),
    Object(Vec<Value>), // only the values, the keys don't matter
}

fn parse_string(s: &[u8], i: &mut usize) -> String {
    let start = *i + 1;
    let mut end = start;
    while s[end] != b'"' {
        end += 1;
    }
    *i = end + 1;
    String::from_utf8(s[start..end].to_vec()).unwrap()
}

fn parse_value(s: &[u8], i: &mut usize) -> Value {
    if s[*i] == b'[' || s[*i] == b'{' {
        let is_object = s[*i] == b'{';
        let closing = if is_object { b'}' } else { b']' };
        let mut children = vec![];
        *i += 1;
        while s[*i] != closing {
            if s[*i] == b',' {
                *i += 1;
            }
            if is_object {
                parse_string(s, i); // the key
                *i += 1; // the colon
            }
            children.push(parse_value(s, i));
        }
        *i += 1;
        if is_object { Value::Object(children) } else { Value::Array(children) }
    } else if s[*i] == b'"' {
        Value::Text(parse_string(s, i))
    } else {
        let start = *i;
        while s[*i] == b'-' || s[*i].is_ascii_digit() {
            *i += 1;
        }
        Value::Number(std::str::from_utf8(&s[start..*i]).unwrap().parse().unwrap())
    }
}

fn sum_numbers(obj: &Value, ignore_red: bool) -> i64 {
    // Walk the JSON recursively and add up every number found
    match obj {
        Value::Number(number) => *number,
        Value::Text(_) => 0,
        Value::Array(children) => children.iter().map(|elem| sum_numbers(elem, ignore_red)).sum(),
        Value::Object(children) => {
            // Part 2: skip any object (not array) that has "red" as a value
            if ignore_red && children.iter().any(|value| matches!(value, Value::Text(text) if text == "red")) {
                return 0;
            }
            children.iter().map(|value| sum_numbers(value, ignore_red)).sum()
        }
    }
}

fn main() {
    let file_content = read_text();

    let mut i = 0;
    let json_obj = parse_value(file_content.as_bytes(), &mut i);

    let part_1_res = sum_numbers(&json_obj, false);
    let part_2_res = sum_numbers(&json_obj, true);

    println!("Part 1 res: {}", part_1_res);
    println!("Part 2 res: {}", part_2_res);
}
