import sys

file_content = open(sys.argv[1]).read().strip()

max_balls = {
    "red": 12,
    "green": 13,
    "blue": 14
}


all_games = []
invalid_games = []
part_2_res = 0
for line in file_content.splitlines():
    split_line = line.split(":")
    
    game_id = int(split_line[0].split("Game ")[1])
    all_games.append(game_id)
    sets = split_line[1].split(";")
    
    blues = []
    greens = []
    reds = []
    for curr_set in sets:
        for items in curr_set.split(","):
            ball_colors = items.split(" ")
            num_balls = int(ball_colors[1])
            color = ball_colors[2]
            
            if color == "blue":
                blues.append(num_balls)
            elif color == "red":
                reds.append(num_balls)
            elif color == "green":
                greens.append(num_balls)
            
            if num_balls > max_balls[color]:
                invalid_games.append(game_id)
                # Could add a break but should be commented for part 1 and to 2 be solved in the same run
    
    
    part_2_res += max(blues) * max(greens) * max(reds)


valid_games = list(set(all_games).difference(set(invalid_games)))

print(f"Part 1 res: {sum(valid_games)}")
print(f"Part 2 res: {part_2_res}")