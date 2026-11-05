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

var points = [[Int]](repeating: [Int](repeating: 0, count: 1000), count: 1000)
var points2 = points

for line in fileContent {
    let elems = words(line)
    // "toggle a,b through c,d" has 4 words, "turn on a,b through c,d" has 5
    let action = elems.count == 4 ? "toggle" : elems[1]
    let numsF = words(elems[elems.count - 3], ",").map { Int($0)! }
    let numsT = words(elems[elems.count - 1], ",").map { Int($0)! }

    for x in numsF[0]...numsT[0] {
        for y in numsF[1]...numsT[1] {
            if action == "off" {
                points[x][y] = 0
                points2[x][y] = max(0, points2[x][y] - 1)
            } else if action == "on" {
                points[x][y] = 1
                points2[x][y] += 1
            } else {
                points[x][y] = 1 - points[x][y]
                points2[x][y] += 2
            }
        }
    }
}

let part1Res = points.joined().reduce(0, +)
let part2Res = points2.joined().reduce(0, +)

print("Part 1 res: \(part1Res)")
print("Part 2 res: \(part2Res)")
