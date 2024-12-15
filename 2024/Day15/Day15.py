import sys
file_content = open(sys.argv[1]).read().strip()

class Box:
    def __init__(self, positions):
        self.positions = positions
    
    def can_be_updated(self, offset, walls):
        dx, dy = offset
        
        for x, y in self.positions:
            new_x, new_y = x + dx, y + dy
            if (new_x, new_y) in walls:
                return False
        return True
    
    def update_box(self, offset, max_x, max_y):
        new_positions = []
        dx, dy = offset
        for x, y in self.positions:
            new_x, new_y = x + dx, y + dy
            
            if new_x >= 1 and new_x <= max_x and new_y >= 1 and new_y <= max_y:
                new_positions.append((new_x, new_y))
            else:
                new_positions.append((x, y))
        self.positions = new_positions

    def __str__(self):
        return str([(x, y) for x, y in self.positions])

boxes_1 = []
boxes_2 = []
walls_1 = []
walls_2 = []
grid, tmp_movements = file_content.split("\n\n")
grid = grid.split("\n")
grid = [list(line) for line in grid]
grid_2 = []
for x, line in enumerate(grid):
    tmp_line = []
    for y, char in enumerate(line):
        if char == "#":
            walls_1.append((x, y))
            walls_2.append((x, 2 * y+1))
            walls_2.append((x, 2 * y))
            tmp_line.append("#")
            tmp_line.append("#")
        elif char == "O":
            boxes_1.append(Box([(x, y)]))
            boxes_2.append(Box([(x, 2 * y), (x, 2*y + 1)]))
            tmp_line.append("[")
            tmp_line.append("]")
        elif char == ".":
            tmp_line.append(".")
            tmp_line.append(".")
        else:
            tmp_line.append("@")
            tmp_line.append(".")
            
            
    grid_2.append(tmp_line)


movements = ""
for line in tmp_movements.splitlines():
    movements += line
    


def plot_grid(walls, boxes: list[Box], agent_pos, rows, cols, part_1=True):
    i = 0
    for _ in range(rows):
        j = 0
        curr_line = ""
        while j < cols:
            if (i, j) == agent_pos: curr_line += "@"
            elif (i, j) in walls: curr_line += "#"
            elif any([(i, j) in box.positions for box in boxes]):
                if part_1:
                    curr_line += "O"
                else:
                    curr_line += "[]"
                    j += 1
            else:
                curr_line += "."
            j += 1 
        print(curr_line)
        i += 1


def initial_pos(grid):
    curr_pos = None
    for x, line in enumerate(grid):
        for y, char in enumerate(line):
            if char == "@":
                curr_pos = (x, y)
                grid[x][y] = "."
    return curr_pos, grid


curr_pos_1, grid = initial_pos(grid)
curr_pos_2, grid_2 = initial_pos(grid_2)
r_1 = len(grid)
c_1 = len(grid[0])
r_2 = len(grid_2)
c_2 = len(grid_2[0])


offsets = {
    "<": (0, -1),
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0)
}

def box_can_move(box_pos, boxes, direction, walls):
    x, y = box_pos
    dx, dy = offsets[direction]
    while (x, y) not in walls:
        x += dx
        y += dy
        if not any([(x, y) in box.positions for box in boxes]) and (x, y) not in walls: return True
    
    return False

def get_touching_boxes(x, y, dx, dy, boxes):
    touching = set()
    for i, box in enumerate(boxes):
        if any((nx, ny) in box.positions for nx, ny in [(x + dx, y), (x, y + dy)]):
            touching.add(i)
    return touching

def update_boxes(box_pos, direction, walls, boxes: list[Box], rows, cols):
    x, y = box_pos
    dx, dy = offsets[direction]
    
    update_boxes = set()
    current_check = {(x, y)}

    while current_check:
        new_check = set()
        for cx, cy in current_check:
            if (cx, cy) not in walls:
                touching = get_touching_boxes(cx, cy, dx, dy, boxes)
                for idx in touching:
                    if idx not in update_boxes:
                        update_boxes.add(idx)
                        new_check.update(boxes[idx].positions)
        current_check = new_check

    can_move = False
    if all([boxes[idx].can_be_updated(offsets[direction], walls) for idx in update_boxes]):
        can_move = True
        for idx in update_boxes:
            boxes[idx].update_box(offsets[direction], rows - 1, cols - 1)

    return (boxes, can_move)  
    
    

def move(position, direction, walls, boxes: list[Box], rows, cols):
    dx, dy = offsets[direction]
    x, y = position
    new_x, new_y = x + dx, y + dy
    
    if any([(new_x, new_y) in box.positions for box in boxes]) and box_can_move((new_x, new_y), boxes, direction, walls):
        boxes, can_move = update_boxes((new_x, new_y), direction, walls, boxes, rows, cols)
        if can_move:
            return (new_x, new_y), boxes
        else:
            return position, boxes
    elif (new_x, new_y) in walls or any([(new_x, new_y) in box.positions for box in boxes]):
        return position, boxes
    else:
        return (new_x, new_y), boxes


for dir in movements:
    curr_pos_1, boxes_1 = move(curr_pos_1, dir, walls_1, boxes_1, r_1, c_1)
    curr_pos_2, boxes_2 = move(curr_pos_2, dir, walls_2, boxes_2, r_2, c_2)
    

def compute_res(boxes: list[Box]):
    res = 0
    for box in boxes:
        x, y = box.positions[0]
        res += x * 100 + y
    return res

part_1_res = compute_res(boxes_1)
part_2_res = compute_res(boxes_2)

plot_grid(walls_1, boxes_1, curr_pos_1, r_1, c_1)
print("=======================")
plot_grid(walls_2, boxes_2, curr_pos_2, r_2, c_2, False)

print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")