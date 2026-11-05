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

func threeVowels(_ string: String) -> Bool {
    return string.filter { "aeiou".contains($0) }.count >= 3
}

func repeatedChars(_ string: String) -> Bool {
    let chars = Array(string)
    return (1..<chars.count).contains { chars[$0] == chars[$0 - 1] }
}

func substrings(_ string: String) -> Bool {
    return !["ab", "cd", "pq", "xy"].contains { string.contains($0) }
}

func twoGrams(_ string: String) -> Bool {
    let chars = Array(string)
    var firstSeen: [String: Int] = [:]
    for i in 0..<(chars.count - 1) {
        let pair = String(chars[i...(i + 1)])
        if let first = firstSeen[pair] {
            if i - first >= 2 { return true }
        } else {
            firstSeen[pair] = i
        }
    }
    return false
}

func threeGrams(_ string: String) -> Bool {
    let chars = Array(string)
    return (0..<(chars.count - 2)).contains { chars[$0] == chars[$0 + 2] }
}

let fileContent = readLines()

var part1Res = 0
var part2Res = 0

for string in fileContent {
    if threeVowels(string) && repeatedChars(string) && substrings(string) { part1Res += 1 }
    if twoGrams(string) && threeGrams(string) { part2Res += 1 }
}

print("Part 1 res: \(part1Res)")
print("Part 2 res: \(part2Res)")
