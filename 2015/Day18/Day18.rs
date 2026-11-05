fn input_path() -> String {
    std::env::args().nth(1).unwrap()
}

fn read_text() -> String {
    std::fs::read_to_string(input_path()).unwrap().trim_end().to_string()
}

type Grid = Vec<Vec<char>>;

fn get_neighbors(i: usize, j: usize, max_i: usize, max_j: usize) -> Vec<(usize, usize)> {
    let mut neighbors = vec![];
    for a in -1i32..=1 {
        for b in -1i32..=1 {
            let (x, y) = (i as i32 + a, j as i32 + b);
            if (a != 0 || b != 0) && x >= 0 && x < max_i as i32 && y >= 0 && y < max_j as i32 {
                neighbors.push((x as usize, y as usize));
            }
        }
    }
    neighbors
}

fn turn_on_corners(grid: &mut Grid) {
    let (max_i, max_j) = (grid.len() - 1, grid[0].len() - 1);
    for (i, j) in [(0, 0), (0, max_j), (max_i, 0), (max_i, max_j)] {
        grid[i][j] = '#';
    }
}

fn simulate(file_content: &Grid, n: i32, stuck_corners: bool) -> usize {
    let mut grid = file_content.clone(); // Work on a copy so each part starts from the input
    if stuck_corners {
        turn_on_corners(&mut grid);
    }

    for _ in 0..n {
        let mut change = vec![];
        for i in 0..grid.len() {
            for j in 0..grid[i].len() {
                let on = get_neighbors(i, j, grid.len(), grid[0].len())
                    .iter()
                    .filter(|(x, y)| grid[*x][*y] == '#')
                    .count();

                if grid[i][j] == '#' && on != 2 && on != 3 {
                    change.push((i, j));
                } else if grid[i][j] == '.' && on == 3 {
                    change.push((i, j));
                }
            }
        }

        // All lights change at the same time, so only apply the changes after checking every light
        for (i, j) in change {
            grid[i][j] = if grid[i][j] == '#' { '.' } else { '#' };
        }

        if stuck_corners {
            turn_on_corners(&mut grid);
        }
    }

    grid.iter().flatten().filter(|light| **light == '#').count()
}

fn main() {
    let file_content: Grid = read_text().lines().map(|line| line.chars().collect()).collect();

    let is_example = input_path().contains("example");
    let part_1_res = simulate(&file_content, if is_example { 4 } else { 100 }, false);
    let part_2_res = simulate(&file_content, if is_example { 5 } else { 100 }, true);

    println!("Part 1 res: {}", part_1_res);
    println!("Part 2 res: {}", part_2_res);
}
