import CryptoKit
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
var part1Done = false

var count = 1
while true {
    let res = Array(Insecure.MD5.hash(data: Data("\(fileContent)\(count)".utf8)))
    // Each byte is two hex digits
    let fiveZeros = res[0] == 0 && res[1] == 0 && res[2] < 16
    let sixZeros = res[0] == 0 && res[1] == 0 && res[2] == 0
    if fiveZeros && !part1Done {
        part1Res = count
        part1Done = true
    }
    if sixZeros {
        part2Res = count
        break
    }
    count += 1
}

print("Part 1 res: \(part1Res)")
print("Part 2 res: \(part2Res)")
