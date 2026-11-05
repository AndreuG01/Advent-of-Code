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

let target = [
    "children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0,
    "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1,
]

for (i, rawLine) in fileContent.enumerated() {
    let line = rawLine.replacingOccurrences(of: ":", with: "").replacingOccurrences(of: ",", with: "")
    let parts = Array(words(line).dropFirst(2))

    var matches = true
    var matches2 = true
    var idx = 0
    while idx < parts.count {
        let detect = parts[idx]
        let val = Int(parts[idx + 1])!
        let expected = target[detect]!
        if expected != val { matches = false }

        // Part 2: cats and trees are lower bounds, pomeranians and goldfish upper bounds
        if detect == "cats" || detect == "trees" {
            if val <= expected { matches2 = false }
        } else if detect == "pomeranians" || detect == "goldfish" {
            if val >= expected { matches2 = false }
        } else if expected != val {
            matches2 = false
        }
        idx += 2
    }
    if matches { part1Res = i + 1 }
    if matches2 { part2Res = i + 1 }
}

print("Part 1 res: \(part1Res)")
print("Part 2 res: \(part2Res)")
