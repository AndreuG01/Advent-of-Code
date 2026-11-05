import sys

file_content = open(sys.argv[1]).read().strip()

part_1_res = 0
part_2_res = 0

def increasing_straight(string) -> bool:
    for i in range(2, len(string)):
       a, b, c = ord(string[i]), ord(string[i - 1]), ord(string[i - 2])
       if b == c + 1 and a == b + 1: return True
    
    return False

def letters(string) -> bool:
    for char in string:
        if char in ["i", "o", "l"]: return False
    return True


def two_grams(string) -> bool:
    found = 0
    i = 1
    while i < len(string):
        if string[i] == string[i - 1]:
            found += 1
            i += 2  # skip so the pairs can't overlap
        else:
            i += 1
    return found >= 2


def is_valid(string):
    return increasing_straight(string) and two_grams(string) and letters(string)


def increment(string) -> str:
    chars = list(string)
    i = len(chars) - 1
    while i >= 0:
        if chars[i] == "z":
            chars[i] = "a"  # wrap around and carry to the next letter on the left
            i -= 1
        else:
            chars[i] = chr(ord(chars[i]) + 1)
            break
    return "".join(chars)


    
string = increment(file_content)
while not is_valid(string):
    string = increment(string)
part_1_res = string


part_2_res = increment(part_1_res)
while not is_valid(part_2_res):
    part_2_res = increment(part_2_res)
    

print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")
