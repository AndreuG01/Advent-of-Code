fn input_path() -> String {
    std::env::args().nth(1).unwrap()
}

fn read_text() -> String {
    std::fs::read_to_string(input_path()).unwrap().trim_end().to_string()
}

fn without(weights: &[i64], group: &[i64]) -> Vec<i64> {
    let mut rest = weights.to_vec();
    for weight in group {
        let position = rest.iter().position(|elem| elem == weight).unwrap();
        rest.remove(position);
    }
    rest
}

// All groups of exactly size packages that add up to target
fn combinations(weights: &[i64], start: usize, size: usize, target: i64, curr: &mut Vec<i64>, groups: &mut Vec<Vec<i64>>) {
    if size == 0 {
        if target == 0 {
            groups.push(curr.clone());
        }
        return;
    }
    for i in start..weights.len() {
        if weights[i] > target {
            continue;
        }
        curr.push(weights[i]);
        combinations(weights, i + 1, size - 1, target - weights[i], curr, groups);
        curr.pop();
    }
}

fn groups_of_size(weights: &[i64], size: usize, target: i64) -> Vec<Vec<i64>> {
    let mut groups = vec![];
    combinations(weights, 0, size, target, &mut vec![], &mut groups);
    groups
}

fn can_split(weights: &[i64], num_groups: i64, target: i64) -> bool {
    if num_groups == 1 {
        return weights.iter().sum::<i64>() == target;
    }
    for size in 1..=weights.len() {
        for group in groups_of_size(weights, size, target) {
            if can_split(&without(weights, &group), num_groups - 1, target) {
                return true;
            }
        }
    }
    false
}

fn prod(group: &[i64]) -> i64 {
    group.iter().product()
}

fn best_entanglement(weights: &[i64], num_groups: i64) -> i64 {
    let target = weights.iter().sum::<i64>() / num_groups;
    // Sizes go up, so the first size with a valid group has the fewest packages
    for size in 1..=weights.len() {
        let mut groups = groups_of_size(weights, size, target);
        groups.sort_by_key(|group| prod(group));
        for group in groups {
            // The rest of the packages also have to split into equal groups
            if can_split(&without(weights, &group), num_groups - 1, target) {
                return prod(&group);
            }
        }
    }
    panic!("No valid split");
}

fn main() {
    let file_content = read_text();

    let weights: Vec<i64> = file_content.lines().map(|line| line.parse().unwrap()).collect();

    let part_1_res = best_entanglement(&weights, 3);
    let part_2_res = best_entanglement(&weights, 4);

    println!("Part 1 res: {}", part_1_res);
    println!("Part 2 res: {}", part_2_res);
}
