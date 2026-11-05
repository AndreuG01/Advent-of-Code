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

let nums = fileContent.components(separatedBy: CharacterSet.decimalDigits.inverted).filter { !$0.isEmpty }.map { Int($0)! }
let row = nums[0]
let col = nums[1]

// Codes fill the grid by diagonals: (row, col) is on diagonal row + col - 1,
// and all the diagonals before it hold 1 + 2 + ... + (diagonal - 1) codes
let diagonal = row + col - 1
let position = diagonal * (diagonal - 1) / 2 + col

var code = 20151125
for _ in 0..<(position - 1) {
    code = code * 252533 % 33554393
}

let part1Res = code
let part2Res = 0

print("Part 1 res: \(part1Res)")
print("Part 2 res: \(part2Res)")
