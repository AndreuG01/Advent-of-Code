use std::collections::{BTreeSet, HashMap};

fn input_path() -> String {
    std::env::args().nth(1).unwrap()
}

fn read_text() -> String {
    std::fs::read_to_string(input_path()).unwrap().trim_end().to_string()
}

fn permutations(items: &[String]) -> Vec<Vec<String>> {
    if items.len() <= 1 {
        return vec![items.to_vec()];
    }
    let mut result = vec![];
    for i in 0..items.len() {
        let mut rest = items.to_vec();
        let first = rest.remove(i);
        for mut order in permutations(&rest) {
            order.insert(0, first.clone());
            result.push(order);
        }
    }
    result
}

type Happiness = HashMap<(String, String), i32>;

fn total_happiness(arrangement: &[String], happiness: &Happiness) -> i32 {
    let mut total = 0;
    for i in 0..arrangement.len() {
        let a = arrangement[i].clone();
        let b = arrangement[(i + 1) % arrangement.len()].clone(); // the table is round
        total += happiness[&(a.clone(), b.clone())] + happiness[&(b, a)];
    }
    total
}

fn best_arrangement(people: &BTreeSet<String>, happiness: &Happiness) -> i32 {
    // The table is round, so rotations are the same seating: fix the first
    // person and only try every order of the rest
    let people: Vec<String> = people.iter().cloned().collect();
    permutations(&people[1..])
        .into_iter()
        .map(|mut order| {
            order.insert(0, people[0].clone());
            total_happiness(&order, happiness)
        })
        .max()
        .unwrap()
}

fn main() {
    let file_content = read_text();

    // happiness[(a, b)] = how much a's happiness changes when sitting next to b
    let mut happiness = HashMap::new();
    let mut people = BTreeSet::new();
    for line in file_content.lines() {
        // e.g. "Alice would gain 54 happiness units by sitting next to Bob."
        let words: Vec<&str> = line.trim_end_matches('.').split(' ').collect();
        let person = words[0].to_string();
        let neighbour = words[words.len() - 1].to_string();
        let amount: i32 = words[3].parse().unwrap();
        happiness.insert((person.clone(), neighbour.clone()), if words[2] == "gain" { amount } else { -amount });
        people.insert(person);
        people.insert(neighbour);
    }

    let part_1_res = best_arrangement(&people, &happiness);

    // Part 2: add yourself, with 0 happiness towards and from everyone
    for person in &people {
        happiness.insert(("Me".to_string(), person.clone()), 0);
        happiness.insert((person.clone(), "Me".to_string()), 0);
    }
    people.insert("Me".to_string());
    let part_2_res = best_arrangement(&people, &happiness);

    println!("Part 1 res: {}", part_1_res);
    println!("Part 2 res: {}", part_2_res);
}
