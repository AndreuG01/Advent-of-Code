import sys

file_content = open(sys.argv[1]).read().splitlines()

part_1_res = 0
part_2_res = 0

instructions = [line.replace(",", "").split(" ") for line in file_content]


def run(registers):
    pc = 0
    while 0 <= pc < len(instructions):
        instruction = instructions[pc]
        action = instruction[0]
        if action == "hlf":
            registers[instruction[1]] //= 2
        elif action == "tpl":
            registers[instruction[1]] *= 3
        elif action == "inc":
            registers[instruction[1]] += 1
        elif action == "jmp":
            pc += int(instruction[1])
            continue
        elif action == "jie" and registers[instruction[1]] % 2 == 0:
            pc += int(instruction[2])
            continue
        elif action == "jio" and registers[instruction[1]] == 1:  # jump if ONE, not if odd
            pc += int(instruction[2])
            continue
        pc += 1
    return registers


registers = run({"a": 0, "b": 0})
# The puzzle's example asks for register a
part_1_res = registers["a"] if "example" in sys.argv[1] else registers["b"]

# Part 2: same program, but register a starts at 1
part_2_res = run({"a": 1, "b": 0})["b"]


print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")
