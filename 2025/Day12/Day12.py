import sys
import re


region_regex = re.compile(r'^(\d+)x(\d+):\s*([\d ]+)$')


def orientations(cells: set[tuple[int, int]]) -> list[list[tuple[int, int]]]:
    # All rotations and flips of a shape, without duplicates. Each one is stored
    # relative to its first cell in reading order, which is the cell that will be
    # anchored on the first free cell of the region while searching.
    result = set()
    current = cells
    for _ in range(4):
        current = {(c, -r) for r, c in current}
        for shape in (current, {(r, -c) for r, c in current}):
            ordered = sorted(shape)
            r0, c0 = ordered[0]
            result.add(tuple((r - r0, c - c0) for r, c in ordered))
    return [list(shape) for shape in result]


def parse(content: str):
    shapes = []
    regions = []
    for block in content.split("\n\n"):
        lines = block.strip().splitlines()
        if region_regex.match(lines[0]):
            for line in lines:
                width, height, counts = region_regex.match(line).groups()
                regions.append((int(width), int(height), [int(num) for num in counts.split()]))
        else:
            cells = {(r, c) for r, row in enumerate(lines[1:]) for c, char in enumerate(row) if char == "#"}
            shapes.append(cells)
    return shapes, regions


def can_fit(width: int, height: int, counts: list[int], shapes: list[set], shape_orientations: list[list]) -> bool:
    area = width * height
    needed = sum(count * len(shape) for count, shape in zip(counts, shapes))
    # Not enough room for all the # cells, no matter how they are arranged
    if needed > area:
        return False
    # Every present fits inside a 3x3 box, so if there are enough boxes to give
    # each present its own one there is nothing to search
    if (width // 3) * (height // 3) >= sum(counts):
        return True

    # Otherwise search: go through the cells in reading order and decide for the
    # first undecided one whether it is covered by a present anchored there or
    # left empty. Leaving a cell empty is only allowed while there is spare room.
    full = (1 << area) - 1
    failed = set()

    def search(grid: int, counts: tuple[int, ...], slack: int) -> bool:
        if not any(counts):
            return True
        if (grid, counts) in failed:
            return False
        free = ~grid & full
        pos = (free & -free).bit_length() - 1
        r, c = divmod(pos, width)

        for i, count in enumerate(counts):
            if not count:
                continue
            next_counts = counts[:i] + (count - 1,) + counts[i + 1:]
            for shape in shape_orientations[i]:
                mask = 0
                for dr, dc in shape:
                    rr, cc = r + dr, c + dc
                    if not (0 <= rr < height and 0 <= cc < width) or grid >> (rr * width + cc) & 1:
                        break
                    mask |= 1 << (rr * width + cc)
                else:
                    if search(grid | mask, next_counts, slack):
                        return True

        if slack > 0 and search(grid | (1 << pos), counts, slack - 1):
            return True

        failed.add((grid, counts))
        return False

    return search(0, tuple(counts), area - needed)


file_content = open(sys.argv[1]).read().strip()
shapes, regions = parse(file_content)
shape_orientations = [orientations(shape) for shape in shapes]

part_1_res = 0
for width, height, counts in regions:
    fits = can_fit(width, height, counts, shapes, shape_orientations)
    print(f"{width}x{height}: {counts} -> {'fits' if fits else 'does not fit'}")
    part_1_res += fits

print(f"Part 1 res: {part_1_res}")
