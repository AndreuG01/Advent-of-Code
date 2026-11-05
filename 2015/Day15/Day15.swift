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

func combinationsSum(_ numElems: Int, _ total: Int, _ amounts: inout [Int], _ visit: ([Int]) -> Void) {
    if numElems == 1 {
        // The last value has to be whatever is left
        amounts.append(total)
        visit(amounts)
        amounts.removeLast()
        return
    }
    for first in 0...total {
        amounts.append(first)
        combinationsSum(numElems - 1, total - first, &amounts, visit)
        amounts.removeLast()
    }
}

func dot(_ prop: [Int], _ amounts: [Int]) -> Int {
    return zip(prop, amounts).reduce(0) { $0 + $1.0 * $1.1 }
}

let fileContent = readLines()

var multipliers: [[Int]] = [[], [], [], []]
var calories: [Int] = []

for line in fileContent {
    let splitedElems = words(line.replacingOccurrences(of: ",", with: ""))
    multipliers[0].append(Int(splitedElems[2])!)
    multipliers[1].append(Int(splitedElems[4])!)
    multipliers[2].append(Int(splitedElems[6])!)
    multipliers[3].append(Int(splitedElems[8])!)
    calories.append(Int(splitedElems[10])!)
}

var part1Res = 0
var part2Res = 0

var amounts: [Int] = []
combinationsSum(fileContent.count, 100, &amounts) { curr in
    var currRes = 1
    for prop in multipliers {
        currRes *= max(dot(prop, curr), 0)
    }
    part1Res = max(part1Res, currRes)
    // Part 2: only cookies with exactly 500 calories
    if dot(calories, curr) == 500 {
        part2Res = max(part2Res, currRes)
    }
}

print("Part 1 res: \(part1Res)")
print("Part 2 res: \(part2Res)")
