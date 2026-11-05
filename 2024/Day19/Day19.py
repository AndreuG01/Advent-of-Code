import sys
from functools import cache

file_content = open(sys.argv[1]).read().strip()
patterns_section, designs_section = file_content.split("\n\n")

patterns = [pattern.strip() for pattern in patterns_section.split(",")]
designs = designs_section.splitlines()


@cache
def count_arrangements(design: str) -> int:
    # Every arrangement starts with some towel that matches the beginning of
    # the design, followed by any arrangement of what is left
    if not design:
        return 1
    return sum(
        count_arrangements(design[len(pattern):])
        for pattern in patterns
        if design.startswith(pattern)
    )


arrangements = [count_arrangements(design) for design in designs]

part_1_res = sum(1 for ways in arrangements if ways > 0)
part_2_res = sum(arrangements)

print(f"Part 1 res: {part_1_res}")
print(f"Part 2 res: {part_2_res}")
