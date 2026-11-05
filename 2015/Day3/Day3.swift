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

struct Position: Hashable {
    var x = 0
    var y = 0

    func moved(_ elem: Character) -> Position {
        switch elem {
        case "^": return Position(x: x, y: y + 1)
        case ">": return Position(x: x + 1, y: y)
        case "<": return Position(x: x - 1, y: y)
        default: return Position(x: x, y: y - 1)
        }
    }
}

let fileContent = readText()

var currPos = Position()
var uniquePos: Set<Position> = [currPos]
for elem in fileContent {
    currPos = currPos.moved(elem)
    uniquePos.insert(currPos)
}
let part1Res = uniquePos.count

var santas = [Position(), Position()]  // Santa and Robo-Santa
var visited: Set<Position> = [Position()]
for (i, elem) in fileContent.enumerated() {
    santas[i % 2] = santas[i % 2].moved(elem)
    visited.insert(santas[i % 2])
}
let part2Res = visited.count

print("Part 1 res: \(part1Res)")
print("Part 2 res: \(part2Res)")
