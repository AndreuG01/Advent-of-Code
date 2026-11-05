import sys

file_content = [list(line) for line in open(sys.argv[1]).read().splitlines()]

def get_neighbors(i, j, max_i=len(file_content), max_j=len(file_content[0])):
    return [
        (i - 1, j - 1) if i - 1 >= 0 and j - 1 >= 0 else None,
        (i - 1, j) if i-1 >= 0 else None,
        (i - 1, j + 1) if i-1 >= 0 and j + 1 < max_j else None,
        (i, j - 1) if j-1>= 0 else None,
        (i, j + 1) if j+1 < max_j else None,
        (i + 1, j - 1) if i+1 < max_i and j -1>=0 else None,
        (i + 1, j) if i+1 < max_i else None,
        (i + 1, j + 1) if i+1 < max_i and j+1 < max_j else None
    ]
    

def turn_on_corners(grid):
    max_i, max_j = len(grid) - 1, len(grid[0]) - 1
    for i, j in [(0, 0), (0, max_j), (max_i, 0), (max_i, max_j)]:
        grid[i][j] = "#"


def simulate(grid, N, stuck_corners=False):
    grid = [row[:] for row in grid]  # Work on a copy so each part starts from the input
    if stuck_corners: turn_on_corners(grid)

    turn = 0
    while turn < N:
        change = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                neighbors = get_neighbors(i, j)
                on = 0
                for n in neighbors:
                    if n is not None and grid[n[0]][n[1]] == "#":
                        on += 1

                if grid[i][j] == "#" and on not in [2, 3]:
                    change.append((i, j))
                elif grid[i][j] == "." and on == 3:
                    change.append((i, j))

        # All lights change at the same time, so only apply the changes after checking every light
        for i, j in change:
            grid[i][j] = "." if grid[i][j] == "#" else "#"

        if stuck_corners: turn_on_corners(grid)
        turn += 1

    return sum([row.count("#") for row in grid])


is_example = "example" in sys.argv[1]
part_1_res = simulate(file_content, 4 if is_example else 100)
part_2_res = simulate(file_content, 5 if is_example else 100, stuck_corners=True)


print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")
