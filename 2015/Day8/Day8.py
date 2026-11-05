import sys
import ast
import json

file_content = open(sys.argv[1]).read().splitlines()

part_1_res = 0
part_2_res = 0


for line in file_content:
    part_1_res += len(line) - len(ast.literal_eval(line))
    # json.dumps re-encodes the line: wraps it in quotes and escapes " and \
    part_2_res += len(json.dumps(line)) - len(line)


print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")
