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

struct Reindeer {
    let speed: Int
    let flyTime: Int
    let restTime: Int
    var distance = 0
    var secondsLeft: Int  // in the current state
    var flying = true
    var points = 0
}

let fileContent = readLines()

var results: [Reindeer] = []
for line in fileContent {
    let elems = words(line)
    let flyTime = Int(elems[6])!
    results.append(Reindeer(speed: Int(elems[3])!, flyTime: flyTime, restTime: Int(elems[elems.count - 2])!, secondsLeft: flyTime))
}

let N = 2503
var maxVal = 0

for _ in 0..<N {
    for i in 0..<results.count {
        if results[i].flying { results[i].distance += results[i].speed }
        results[i].secondsLeft -= 1

        if results[i].secondsLeft == 0 {
            // Switch between flying and resting
            results[i].flying.toggle()
            results[i].secondsLeft = results[i].flying ? results[i].flyTime : results[i].restTime
        }
    }
    maxVal = results.map { $0.distance }.max()!
    for i in 0..<results.count where results[i].distance == maxVal {
        results[i].points += 1
    }
}

let part1Res = maxVal
let part2Res = results.map { $0.points }.max()!

print("Part 1 res: \(part1Res)")
print("Part 2 res: \(part2Res)")
