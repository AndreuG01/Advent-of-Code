import sys
from itertools import combinations
import numpy as np


def parse_line(line: str) -> tuple[int, int]:
    x, y = line.split(",")
    return int(x), int(y)


file_content = open(sys.argv[1]).read().strip()
file_content = file_content.splitlines()

# Coordinates come first; a blank line (followed by an optional diagram) marks the end of them
coord_lines = []
for line in file_content:
    if not line.strip():
        break
    coord_lines.append(line)

points = [parse_line(line) for line in coord_lines]

# Any two points can be the opposite corners of a rectangle, regardless of
# whether other points lie on or inside it. The area is inclusive of both
# the start and end coordinates.
max_area = 0
best_rect = None
for (x1, y1), (x2, y2) in combinations(points, 2):
    area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
    if area > max_area:
        max_area = area
        best_rect = ((x1, y1), (x2, y2))

print(f"Largest rectangle: {best_rect}")
print(f"Part 1 res: {max_area}")

# Part 2: the points trace the walls of a room (in order, closing back to the
# start), so the rectangle now has to stay entirely inside that room instead
# of just being allowed to sit on top of other points.
n = len(points)
edges = [(points[i], points[(i + 1) % n]) for i in range(n)]

vertical = [(x1, min(y1, y2), max(y1, y2)) for (x1, y1), (x2, y2) in edges if x1 == x2]
horizontal = [(y1, min(x1, x2), max(x1, x2)) for (x1, y1), (x2, y2) in edges if y1 == y2]

vx, vylo, vyhi = (np.array(col) for col in zip(*vertical))
hy, hxlo, hxhi = (np.array(col) for col in zip(*horizontal))


def point_in_room(x: float, y: float) -> bool:
    inside = False
    x1, y1 = points[-1]
    for x2, y2 in points:
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1:
            inside = not inside
        x1, y1 = x2, y2
    return inside


def rect_fits_in_room(xlo: int, xhi: int, ylo: int, yhi: int) -> bool:
    # A wall cutting through the rectangle's interior means part of it lies outside the room
    if np.any((vx > xlo) & (vx < xhi) & (np.maximum(ylo, vylo) < np.minimum(yhi, vyhi))):
        return False
    if np.any((hy > ylo) & (hy < yhi) & (np.maximum(xlo, hxlo) < np.minimum(xhi, hxhi))):
        return False
    # No wall crosses it, so the rectangle is either entirely inside or entirely outside the room
    return point_in_room((xlo + xhi) / 2, (ylo + yhi) / 2)


max_area = 0
best_rect = None
for (x1, y1), (x2, y2) in combinations(points, 2):
    xlo, xhi = min(x1, x2), max(x1, x2)
    ylo, yhi = min(y1, y2), max(y1, y2)
    area = (xhi - xlo + 1) * (yhi - ylo + 1)
    if area <= max_area:
        continue

    if not rect_fits_in_room(xlo, xhi, ylo, yhi):
        continue

    max_area = area
    best_rect = ((x1, y1), (x2, y2))

print(f"Largest rectangle inside the room: {best_rect}")
print(f"Part 2 res: {max_area}")
