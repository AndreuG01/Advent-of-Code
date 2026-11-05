import sys
import json

file_content = open(sys.argv[1]).read().strip()


json_obj = json.loads(file_content)



part_1_res = 0
part_2_res = 0


def sum_numbers(obj, ignore_red=False) -> int:
    # Walk the JSON recursively and add up every number found
    if isinstance(obj, int):
        return obj
    if isinstance(obj, list):
        return sum(sum_numbers(elem, ignore_red) for elem in obj)
    if isinstance(obj, dict):
        # Part 2: skip any object (not array) that has "red" as a value
        if ignore_red and "red" in obj.values():
            return 0
        return sum(sum_numbers(value, ignore_red) for value in obj.values())
    return 0  # strings


part_1_res = sum_numbers(json_obj)
part_2_res = sum_numbers(json_obj, ignore_red=True)


print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")
