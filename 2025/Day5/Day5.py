import sys


file_content = open(sys.argv[1]).read().strip()

file_content = file_content.splitlines()


fresh_ingredients = []

idx = 0
for line in file_content:
    idx += 1
    if line == "":
        break
    ingredients = line.split("-")
    fresh_ingredients.append([int(ingredients[0]), int(ingredients[1])])


fresh_ingredients = list(sorted(fresh_ingredients, key=lambda x: x[0]))

overlapping_ingredients = []
current = fresh_ingredients[0]
for interval in fresh_ingredients[1:]:
    if interval[0] <= current[1]:
        current[1] = max(current[1], interval[1])
    else:
        overlapping_ingredients.append(current)
        current = interval

overlapping_ingredients.append(current)

# print(fresh_ingredients)
part_1_res = 0
for i in range(idx, len(file_content)):
    curr_ingredient = int(file_content[i])
    for ingredient in fresh_ingredients:
        # print(curr_ingredient, ingredient)
        if curr_ingredient >= ingredient[0] and curr_ingredient <= ingredient[1]:
            part_1_res += 1
            # print("True")
            break
        

print(f"Part 1 res: {part_1_res}")

part_2_res = sum([ingredient[1] - ingredient[0] + 1 for ingredient in overlapping_ingredients])
print(f"Part 2 res: {part_2_res}")