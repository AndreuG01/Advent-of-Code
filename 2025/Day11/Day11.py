import sys
from functools import cache

sys.setrecursionlimit(10_000)


file_content = open(sys.argv[1]).read().strip()
file_content = file_content.splitlines()

graph = {}
for line in file_content:
    device, outputs = line.split(":")
    graph[device.strip()] = outputs.split()


@cache
def count_paths(device: str, target: str) -> int:
    # Data only flows forward, so the graph has no cycles and the number of
    # paths from a device is the sum of the paths from each of its outputs
    if device == target:
        return 1
    return sum(count_paths(output, target) for output in graph.get(device, []))


# Each example only contains the devices needed by one of the parts
if "you" in graph:
    part_1_res = count_paths("you", "out")
    print(f"Part 1 res: {part_1_res}")

# Part 2: paths from svr to out that go through both dac and fft. Since there
# are no cycles, they can only be visited in one of the two orders, so split
# every path at those two devices and multiply the counts of each segment.
if "svr" in graph:
    part_2_res = (
        count_paths("svr", "dac") * count_paths("dac", "fft") * count_paths("fft", "out")
        + count_paths("svr", "fft") * count_paths("fft", "dac") * count_paths("dac", "out")
    )
    print(f"Part 2 res: {part_2_res}")
