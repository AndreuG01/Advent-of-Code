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

func lookAndSay(_ s: [UInt8]) -> [UInt8] {
    var count = 1
    var val = s[0]
    var newStr: [UInt8] = []
    newStr.reserveCapacity(s.count * 2)
    for i in 1..<s.count {
        if s[i] == val {
            count += 1
        } else {
            newStr.append(contentsOf: String(count).utf8)
            newStr.append(val)
            count = 1
        }
        val = s[i]
    }
    newStr.append(contentsOf: String(count).utf8)
    newStr.append(val)
    return newStr
}

var seq = Array(readText().utf8)

var part1Res = 0

for i in 0..<50 {
    seq = lookAndSay(seq)
    if i == 39 { part1Res = seq.count }
}
let part2Res = seq.count

print("Part 1 res: \(part1Res)")
print("Part 2 res: \(part2Res)")
