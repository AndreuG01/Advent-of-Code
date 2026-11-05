import sys

file_content = open(sys.argv[1]).read().strip()
file_content = file_content.splitlines()

register_a = int(file_content[0].split(":")[1][1:])
register_b = int(file_content[1].split(":")[1][1:])
register_c = int(file_content[2].split(":")[1][1:])
program = [int(num) for num in file_content[4].split(":")[1][1:].split(",")]

print(f"A: {register_a}")
print(f"B: {register_b}")
print(f"C: {register_c}")
print(f"{program}")


def run(register_a: int, register_b: int, register_c: int) -> list[int]:
    combo = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: register_a,
        5: register_b,
        6: register_c,
        7: "invalid"
    }

    instruction_counter = 0

    outputs = []

    while instruction_counter < len(program):
        opcode = program[instruction_counter]
        operand = program[instruction_counter + 1]
        if opcode == 0:
            register_a = register_a // (2 ** combo[operand])

        elif opcode == 1:
            # XOR (^ operator in python)
            register_b ^= operand

        elif opcode == 2:
            register_b = combo[operand] % 8

        elif opcode == 3:
            if register_a != 0:
                instruction_counter = operand
                continue
        elif opcode == 4:
            register_b ^= register_c
        elif opcode == 5:
            outputs.append(combo[operand] % 8)
        elif opcode == 6:
            register_b = register_a // (2 ** combo[operand])
        elif opcode == 7:
            register_c = register_a // (2 ** combo[operand])

        instruction_counter += 2
        combo[4] = register_a
        combo[5] = register_b
        combo[6] = register_c

    return outputs


part_1_res = ",".join([str(val) for val in run(register_a, register_b, register_c)])
print(f"Part 1 res: {part_1_res}")

# Part 2: the program is a loop that outputs one value and then divides A by
# 8 (adv 3) until A is 0. So the last output only depends on the highest 3
# bits of A, the one before it on the next 3 bits, and so on. Build A from
# the end of the program backwards, 3 bits at a time, keeping every value
# whose output matches the tail of the program seen so far.
candidates = [0]
for i in range(len(program) - 1, -1, -1):
    candidates = [
        candidate * 8 + bits
        for candidate in candidates
        for bits in range(8)
        if run(candidate * 8 + bits, register_b, register_c) == program[i:]
    ]

candidates = [a for a in candidates if a > 0]
if candidates:
    part_2_res = min(candidates)
    print(f"Part 2 res: {part_2_res}")
else:
    print("Part 2: no value of A makes this program output itself")
