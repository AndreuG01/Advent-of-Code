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

let backslash = UInt8(ascii: "\\")
let quote = UInt8(ascii: "\"")

func memoryLength(_ line: String) -> Int {
    let inner = Array(line.utf8).dropFirst().dropLast().map { $0 }  // drop the surrounding quotes
    var i = 0
    var memLen = 0
    while i < inner.count {
        if inner[i] == backslash {
            i += inner[i + 1] == UInt8(ascii: "x") ? 4 : 2
        } else {
            i += 1
        }
        memLen += 1
    }
    return memLen
}

let fileContent = readLines()

var part1Res = 0
var part2Res = 0

for line in fileContent {
    part1Res += line.utf8.count - memoryLength(line)
    // Encoding adds the 2 new quotes and one backslash for each " and backslash
    part2Res += 2 + line.utf8.filter { $0 == quote || $0 == backslash }.count
}

print("Part 1 res: \(part1Res)")
print("Part 2 res: \(part2Res)")
