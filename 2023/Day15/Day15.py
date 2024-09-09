import sys

file_content = open(sys.argv[1]).read().strip()


def get_hash(input: str) -> int:
    
    res = 0
    
    for character in input:
        res += ord(character)
        res *= 17
        res %= 256
    
    return res  
        

def part_1(input):
    res = 0

    for string in input:
        res += get_hash(string)

    return res


def print_boxes(boxes):
    for box in boxes:
        print(f"Box {box}: {boxes[box]}")


def part_2(input):
    
    # Fill the boxes
    boxes = {}
    
    for string in input:
        #print(string)
        if "=" in string:
            new_str = string.split("=")
            box_str = new_str[0]
            box = get_hash(box_str)
            focal_length = new_str[1]
            
            if box not in boxes:
                boxes[box] = [[box_str, focal_length]]
            else:
                present = False
                for elem in boxes[box]:
                    if elem[0] == box_str:
                        present = True
                        elem[1] = focal_length
                
                if not present:
                    boxes[box].append([box_str, focal_length])
        else:
            box_str = string.split("-")[0]
            box = get_hash(box_str)

            if box not in boxes: continue
            else:
                for i in range(len(boxes[box])):
                    if boxes[box][i][0] == box_str:
                        del boxes[box][i]
                        break
                    
                if len(boxes[box]) == 0:
                    del boxes[box]
        
        #print_boxes(boxes)
        
        
        # Compute the final result
        res = 0
        
        for key, val in boxes.items():
            for pos, elem in enumerate(val, start=1):
                focal_length = int(elem[1])
                res += (int(key) + 1) * pos * focal_length

    return res



strings = file_content.split(",")

part_1_res = part_1(strings)
part_2_res = part_2(strings)


print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")