import sys


file_content = open(sys.argv[1]).read().strip()

file_content = file_content.splitlines()

def calculate_joltage(banks: list[list[str]], nr_of_batteries: int) -> int:
    total_joltage = 0
    for bank in banks:
        joltage = ""
        max_index = 0
        for i in range(1, nr_of_batteries + 1):
            end_index = -(nr_of_batteries - i) if (nr_of_batteries - i) != 0 else len(bank)
            max_battery = max(bank[max_index:end_index])
            max_index = bank[max_index:end_index].index(max_battery) + max_index + 1
            joltage += str(max_battery)
        total_joltage += int(joltage)
    return total_joltage


batteries = []

for line in file_content:
    
    batteries.append([x for x in line])

part_1_res = calculate_joltage(batteries, 2)
part_2_res = calculate_joltage(batteries, 12)
print(f"Part 1: {part_1_res}")
print(f"Part 2: {part_2_res}")
