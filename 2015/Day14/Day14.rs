fn input_path() -> String {
    std::env::args().nth(1).unwrap()
}

fn read_text() -> String {
    std::fs::read_to_string(input_path()).unwrap().trim_end().to_string()
}

struct Reindeer {
    speed: i32,
    fly_time: i32,
    rest_time: i32,
    distance: i32,
    seconds_left: i32, // in the current state
    flying: bool,
    points: i32,
}

fn main() {
    let file_content = read_text();

    let mut results = vec![];
    for line in file_content.lines() {
        let elems: Vec<&str> = line.split(' ').collect();
        let fly_time = elems[6].parse().unwrap();
        results.push(Reindeer {
            speed: elems[3].parse().unwrap(),
            fly_time,
            rest_time: elems[elems.len() - 2].parse().unwrap(),
            distance: 0,
            seconds_left: fly_time,
            flying: true,
            points: 0,
        });
    }

    const N: i32 = 2503;
    let mut max_val = 0;

    for _ in 0..N {
        for reindeer in results.iter_mut() {
            if reindeer.flying {
                reindeer.distance += reindeer.speed;
            }
            reindeer.seconds_left -= 1;

            if reindeer.seconds_left == 0 {
                // Switch between flying and resting
                reindeer.flying = !reindeer.flying;
                reindeer.seconds_left = if reindeer.flying { reindeer.fly_time } else { reindeer.rest_time };
            }
        }
        max_val = results.iter().map(|reindeer| reindeer.distance).max().unwrap();
        for reindeer in results.iter_mut() {
            if reindeer.distance == max_val {
                reindeer.points += 1;
            }
        }
    }

    let part_1_res = max_val;
    let part_2_res = results.iter().map(|reindeer| reindeer.points).max().unwrap();

    println!("Part 1 res: {}", part_1_res);
    println!("Part 2 res: {}", part_2_res);
}
