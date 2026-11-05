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

let target = Int(readText())!

var part1Res = 0
var part2Res = 0

// House n gets 10 presents from each elf that divides n, and house target / 10 + 1
// alone gets at least target presents from its own elf, so the answer can't be further away
var limit = target / 10 + 1
var houses = [Int](repeating: 0, count: limit + 1)
for elf in 1...limit {
    for house in stride(from: elf, through: limit, by: elf) {
        houses[house] += elf * 10
    }
}

for house in 1...limit where houses[house] >= target {
    part1Res = house
    break
}

// Part 2: each elf only visits 50 houses, but leaves 11 presents per house
limit = target / 11 + 1
houses = [Int](repeating: 0, count: limit + 1)
for elf in 1...limit {
    for house in stride(from: elf, through: min(elf * 50, limit), by: elf) {
        houses[house] += elf * 11
    }
}

for house in 1...limit where houses[house] >= target {
    part2Res = house
    break
}

print("Part 1 res: \(part1Res)")
print("Part 2 res: \(part2Res)")
