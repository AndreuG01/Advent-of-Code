import Foundation

func inputPath() -> String {
    return CommandLine.arguments[1]
}

func readText() -> String {
    let text = try! String(contentsOfFile: inputPath(), encoding: .utf8)
    return text.trimmingCharacters(in: .whitespacesAndNewlines)
}

func readLines() -> [String] {
    return readText().split(separator: "\n", omittingEmptySubsequences: false).map(String.init)
}

func words(_ line: String, _ separator: Character = " ") -> [String] {
    return line.split(separator: separator).map(String.init)
}

let fileContent = readText()

let nums = fileContent.split(whereSeparator: { $0.isWhitespace }).map { Int($0)! }

var part1Res = 0
var part2Res = 0

let target = inputPath().contains("example") ? 25 : 150

// Each bit of mask says if a container is used, so same-size containers stay different.
// ways[size] counts the matching groups with that many containers.
var ways = [Int](repeating: 0, count: nums.count + 1)
for mask in 1..<(1 << nums.count) {
    var total = 0
    for i in 0..<nums.count where mask & (1 << i) != 0 {
        total += nums[i]
    }
    if total == target { ways[mask.nonzeroBitCount] += 1 }
}

for currRes in ways {
    part1Res += currRes
    // Part 2: sizes go up, so the first size with a match is the minimum
    if part2Res == 0 { part2Res = currRes }
}

print("Part 1 res: \(part1Res)")
print("Part 2 res: \(part2Res)")
