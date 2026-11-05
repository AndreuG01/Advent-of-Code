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

let fileContent = readLines()

var part1Res = 0
var part2Res = 0

for line in fileContent {
    let elem = words(line, "x").map { Int($0)! }
    let l = elem[0]
    let w = elem[1]
    let h = elem[2]

    let aSide1 = l * w
    let aSide2 = w * h
    let aSide3 = h * l

    let pSide1 = 2 * l + 2 * w
    let pSide2 = 2 * w + 2 * h
    let pSide3 = 2 * h + 2 * l

    part1Res += 2 * aSide1 + 2 * aSide2 + 2 * aSide3 + min(aSide2, aSide1, aSide3)
    part2Res += min(pSide1, pSide2, pSide3) + l * w * h
}

print("Part 1 res: \(part1Res)")
print("Part 2 res: \(part2Res)")
