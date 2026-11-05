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

var part1Res = 0
var part2Res = 0
var part2Done = false

for (i, char) in fileContent.enumerated() {
    if char == "(" { part1Res += 1 } else { part1Res -= 1 }
    if part1Res == -1 && !part2Done {
        part2Res = i + 1
        part2Done = true
    }
}

print("Part 1 res: \(part1Res)")
print("Part 2 res: \(part2Res)")
