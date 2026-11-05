fn input_path() -> String {
    std::env::args().nth(1).unwrap()
}

fn read_text() -> String {
    std::fs::read_to_string(input_path()).unwrap().trim_end().to_string()
}

// (cost, damage, armor)
type Item = (i32, i32, i32);

const WEAPONS: [Item; 5] = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)];
const ARMORS: [Item; 5] = [(13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)];
const RINGS: [Item; 6] = [(25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)];

fn player_wins(mut player_hp: i32, player_damage: i32, player_armor: i32, boss: &[i32]) -> bool {
    let (mut boss_hp, boss_damage, boss_armor) = (boss[0], boss[1], boss[2]);
    loop {
        boss_hp -= (player_damage - boss_armor).max(1);
        if boss_hp <= 0 {
            return true;
        }
        player_hp -= (boss_damage - player_armor).max(1);
        if player_hp <= 0 {
            return false;
        }
    }
}

fn loadouts() -> Vec<Vec<Item>> {
    // Exactly 1 weapon, 0 or 1 armor, 0 to 2 rings
    let mut armor_options = vec![vec![]];
    armor_options.extend(ARMORS.iter().map(|armor| vec![*armor]));

    let mut ring_options = vec![vec![]];
    for i in 0..RINGS.len() {
        ring_options.push(vec![RINGS[i]]);
        for j in i + 1..RINGS.len() {
            ring_options.push(vec![RINGS[i], RINGS[j]]);
        }
    }

    let mut result = vec![];
    for weapon in WEAPONS {
        for armor in &armor_options {
            for ring in &ring_options {
                let mut items = vec![weapon];
                items.extend(armor);
                items.extend(ring);
                result.push(items);
            }
        }
    }
    result
}

fn main() {
    let file_content = read_text();

    let boss: Vec<i32> = file_content.lines().map(|line| line.split(": ").nth(1).unwrap().parse().unwrap()).collect();

    let mut part_1_res = i32::MAX;
    let mut part_2_res = 0;

    for items in loadouts() {
        let cost: i32 = items.iter().map(|item| item.0).sum();
        let damage: i32 = items.iter().map(|item| item.1).sum();
        let armor: i32 = items.iter().map(|item| item.2).sum();
        if player_wins(100, damage, armor, &boss) {
            part_1_res = part_1_res.min(cost);
        } else {
            part_2_res = part_2_res.max(cost);
        }
    }

    println!("Part 1 res: {}", part_1_res);
    println!("Part 2 res: {}", part_2_res);
}
