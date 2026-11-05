use std::collections::{BTreeMap, HashMap};

fn input_path() -> String {
    std::env::args().nth(1).unwrap()
}

fn read_text() -> String {
    std::fs::read_to_string(input_path()).unwrap().trim_end().to_string()
}

const MASK: u32 = 0xFFFF; // signals are 16-bit

// Instructions are not in order, so first store how each wire is computed,
// then resolve wires recursively (memoized) when asked for
fn signal(name: &str, circuit: &BTreeMap<String, Vec<String>>, cache: &mut HashMap<String, u32>) -> u32 {
    if let Ok(number) = name.parse() {
        return number;
    }
    if let Some(value) = cache.get(name) {
        return *value;
    }

    let operation = &circuit[name];
    let result = match operation.len() {
        // e.g. "123 -> x" or "lx -> a"
        1 => signal(&operation[0], circuit, cache),
        // NOT x
        2 => !signal(&operation[1], circuit, cache) & MASK,
        _ => {
            let one = signal(&operation[0], circuit, cache);
            let two = signal(&operation[2], circuit, cache);
            match operation[1].as_str() {
                "AND" => one & two,
                "OR" => one | two,
                "LSHIFT" => (one << two) & MASK,
                "RSHIFT" => one >> two,
                action => panic!("Unknown action: {}", action),
            }
        }
    };
    cache.insert(name.to_string(), result);
    result
}

fn main() {
    let file_content = read_text();

    let mut part_1_res = 0;
    let mut part_2_res = 0;

    let mut circuit = BTreeMap::new();
    for line in file_content.lines() {
        let (expr, dest) = line.split_once(" -> ").unwrap();
        circuit.insert(dest.to_string(), expr.split(' ').map(String::from).collect::<Vec<String>>());
    }

    let mut cache = HashMap::new();
    if circuit.contains_key("a") {
        part_1_res = signal("a", &circuit, &mut cache);

        // Part 2: override wire b with part 1's signal, reset all wires and rerun
        circuit.insert("b".to_string(), vec![part_1_res.to_string()]);
        cache.clear();
        part_2_res = signal("a", &circuit, &mut cache);
    } else {
        // The example has no wire "a": show every wire instead
        for wire in circuit.keys() {
            println!("{}: {}", wire, signal(wire, &circuit, &mut cache));
        }
    }

    println!("Part 1 res: {}", part_1_res);
    println!("Part 2 res: {}", part_2_res);
}
