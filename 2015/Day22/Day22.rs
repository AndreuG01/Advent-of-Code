use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashSet};

fn input_path() -> String {
    std::env::args().nth(1).unwrap()
}

fn read_text() -> String {
    std::fs::read_to_string(input_path()).unwrap().trim_end().to_string()
}

// Returns mana, boss, shield, poison, recharge, armor after the effects of a turn
fn apply_effects(mut mana: i32, mut boss: i32, shield: i32, poison: i32, recharge: i32) -> (i32, i32, i32, i32, i32, i32) {
    let armor = if shield > 0 { 7 } else { 0 };
    if poison > 0 {
        boss -= 3;
    }
    if recharge > 0 {
        mana += 101;
    }
    (mana, boss, (shield - 1).max(0), (poison - 1).max(0), (recharge - 1).max(0), armor)
}

// Every spell that can be cast now: (cost, hp, boss, shield, poison, recharge)
fn cast_spells(hp: i32, mana: i32, boss: i32, shield: i32, poison: i32, recharge: i32) -> Vec<(i32, i32, i32, i32, i32, i32)> {
    let mut options = vec![
        (53, hp, boss - 4, shield, poison, recharge),     // Magic Missile
        (73, hp + 2, boss - 2, shield, poison, recharge), // Drain
    ];
    if shield == 0 {
        options.push((113, hp, boss, 6, poison, recharge));
    }
    if poison == 0 {
        options.push((173, hp, boss, shield, 6, recharge));
    }
    if recharge == 0 {
        options.push((229, hp, boss, shield, poison, 5));
    }
    options.retain(|option| option.0 <= mana);
    options
}

fn least_mana(player_hp: i32, player_mana: i32, boss_hp: i32, boss_damage: i32, hard: bool) -> Option<i32> {
    // Dijkstra: always continue from the fight that has spent the least mana so far,
    // so the first won fight taken from the queue is the cheapest one
    let mut queue = BinaryHeap::new();
    queue.push(Reverse((0, player_hp, player_mana, boss_hp, 0, 0, 0)));
    let mut seen = HashSet::new();

    while let Some(Reverse(state)) = queue.pop() {
        let (spent, mut hp, mana, boss, shield, poison, recharge) = state;
        if boss <= 0 {
            return Some(spent);
        }
        if !seen.insert(state) {
            continue;
        }

        // Player turn
        if hard {
            // Part 2: lose 1 HP at the start of each player turn, before effects
            hp -= 1;
            if hp <= 0 {
                continue;
            }
        }

        let (mana, boss, shield, poison, recharge, _) = apply_effects(mana, boss, shield, poison, recharge);
        if boss <= 0 {
            queue.push(Reverse((spent, hp, mana, boss, shield, poison, recharge)));
            continue;
        }

        for (cost, mut new_hp, new_boss, new_shield, new_poison, new_recharge) in cast_spells(hp, mana, boss, shield, poison, recharge) {
            // Boss turn
            let (new_mana, new_boss, new_shield, new_poison, new_recharge, armor) =
                apply_effects(mana - cost, new_boss, new_shield, new_poison, new_recharge);
            if new_boss > 0 {
                new_hp -= (boss_damage - armor).max(1);
                if new_hp <= 0 {
                    continue;
                }
            }
            queue.push(Reverse((spent + cost, new_hp, new_mana, new_boss, new_shield, new_poison, new_recharge)));
        }
    }
    None // the fight can't be won
}

fn show(mana: Option<i32>) -> String {
    mana.map_or("None".to_string(), |mana| mana.to_string())
}

fn main() {
    let file_content = read_text();

    let boss: Vec<i32> = file_content.lines().map(|line| line.split(": ").nth(1).unwrap().parse().unwrap()).collect();
    let (boss_hp, boss_damage) = (boss[0], boss[1]);

    // The puzzle's examples use a weaker player
    let (player_hp, player_mana) = if input_path().contains("example") { (10, 250) } else { (50, 500) };

    let part_1_res = show(least_mana(player_hp, player_mana, boss_hp, boss_damage, false));
    let part_2_res = show(least_mana(player_hp, player_mana, boss_hp, boss_damage, true));

    println!("Part 1 res: {}", part_1_res);
    println!("Part 2 res: {}", part_2_res);
}
