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

fn main() {
    let file_content = read_text();

    // Distances work both ways, so store each pair in both directions
    let mut distances = HashMap::new();
    let mut cities = BTreeSet::new();
    for line in file_content.lines() {
        let parts: Vec<&str> = line.split(' ').collect(); // "London to Dublin = 464"
        let (a, b) = (parts[0].to_string(), parts[2].to_string());
        let dist: i32 = parts[4].parse().unwrap();
        distances.insert((a.clone(), b.clone()), dist);
        distances.insert((b.clone(), a.clone()), dist);
        cities.insert(a);
        cities.insert(b);
    }

    // Few cities, so trying every order is fast enough
    let cities: Vec<String> = cities.into_iter().collect();
    let route_lengths: Vec<i32> = permutations(&cities)
        .iter()
        .map(|route| route.windows(2).map(|pair| distances[&(pair[0].clone(), pair[1].clone())]).sum())
        .collect();

    let part_1_res = route_lengths.iter().min().unwrap();
    let part_2_res = route_lengths.iter().max().unwrap();

    println!("Part 1 res: {}", part_1_res);
    println!("Part 2 res: {}", part_2_res);
}
