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

func increasingStraight(_ string: [UInt8]) -> Bool {
    for i in 2..<string.count {
        let a = string[i], b = string[i - 1], c = string[i - 2]
        if b == c + 1 && a == b + 1 { return true }
    }
    return false
}

func letters(_ string: [UInt8]) -> Bool {
    return !string.contains { Array("iol".utf8).contains($0) }
}

func twoGrams(_ string: [UInt8]) -> Bool {
    var found = 0
    var i = 1
    while i < string.count {
        if string[i] == string[i - 1] {
            found += 1
            i += 2  // skip so the pairs can't overlap
        } else {
            i += 1
        }
    }
    return found >= 2
}

func isValid(_ string: [UInt8]) -> Bool {
    return increasingStraight(string) && twoGrams(string) && letters(string)
}

func increment(_ string: [UInt8]) -> [UInt8] {
    var chars = string
    var i = chars.count - 1
    while i >= 0 {
        if chars[i] == UInt8(ascii: "z") {
            chars[i] = UInt8(ascii: "a")  // wrap around and carry to the next letter on the left
            i -= 1
        } else {
            chars[i] += 1
            break
        }
    }
    return chars
}

let fileContent = Array(readText().utf8)

var part1 = increment(fileContent)
while !isValid(part1) { part1 = increment(part1) }

var part2 = increment(part1)
while !isValid(part2) { part2 = increment(part2) }

let part1Res = String(decoding: part1, as: UTF8.self)
let part2Res = String(decoding: part2, as: UTF8.self)

print("Part 1 res: \(part1Res)")
print("Part 2 res: \(part2Res)")
