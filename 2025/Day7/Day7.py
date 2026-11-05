import sys
import re




file_content = open(sys.argv[1]).read().strip()


file_content = file_content.splitlines()



file_content[0] = [char if char == "." else "|" for char in file_content[0]]
file_content = [
    [char for char in line] for line in file_content
]

print(file_content)

part_1_res = 0
i = 1
while i <= len(file_content) - 1:
    
    for j, char in enumerate(file_content[i]):
        if file_content[i - 1][j] == "|" and char != "^":
            file_content[i][j] = "|"
        elif char == "^":
            if file_content[i - 1][j] == "|": part_1_res += 1
            j_prev = max(0, j - 1)
            j_next = min(len(file_content[i]) - 1, j + 1)
            
            file_content[i][j_prev] = "|"
            file_content[i][j_next] = "|"
    i += 1


for line in file_content:
    print("".join(line))


print(f"Part 1 res: {part_1_res}")

# Part 2: a single tachyon particle takes either the left or the right path at
# every splitter, so count how many timelines reach each column row by row.
grid = open(sys.argv[1]).read().strip().splitlines()

timelines = [0] * len(grid[0])
timelines[grid[0].index("S")] = 1

for row in grid[1:]:
    next_timelines = [0] * len(row)
    for j, count in enumerate(timelines):
        if not count:
            continue
        if row[j] == "^":
            if j - 1 >= 0:
                next_timelines[j - 1] += count
            if j + 1 < len(row):
                next_timelines[j + 1] += count
        else:
            next_timelines[j] += count
    timelines = next_timelines

part_2_res = sum(timelines)
print(f"Part 2 res: {part_2_res}")
