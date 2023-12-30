import sys

def is_valid(sequence, combinations):
    clean_seq = [seq for seq in sequence.split(".") if seq != ""]

    if len(clean_seq) != len(combinations): return False

    for i, seq in enumerate(clean_seq):
        if len(seq) != combinations[i]:
            return False

    return True

def generate_combinations(s, result, current="", index=0):
    if index == len(s):
        result.append(current)
        return

    if s[index] == "?":
        generate_combinations(s, result, current + ".", index + 1)
        generate_combinations(s, result, current + "#", index + 1)
    else:
        generate_combinations(s, result, current + s[index], index + 1)


file_content = open(sys.argv[1]).read().strip().splitlines()


# Brute force does not work for part 2 :(
# Perhaps use dynamic programming?
part1_res = 0
part2_res = 0

count = 0
for line in file_content:
    arrangement = line.split(" ")[0]
    combinations = [int(num) for num in line.split(" ")[1].split(",")]
    results = []
    generate_combinations(arrangement, results)
    # print(f"combinations generated for line {count}: {len(results)}")
    for res in results:
        # print(f"\t{res}")
        if is_valid(res, combinations):
            part1_res += 1
    count += 1

print(f"Part 1 res: {part1_res}")
