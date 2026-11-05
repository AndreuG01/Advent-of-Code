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

func permutations(_ items: [String]) -> [[String]] {
    if items.count <= 1 { return [items] }
    var result: [[String]] = []
    for i in 0..<items.count {
        var rest = items
        let first = rest.remove(at: i)
        for order in permutations(rest) {
            result.append([first] + order)
        }
    }
    return result
}

let fileContent = readLines()

// Distances work both ways, so store each pair in both directions
var distances: [String: Int] = [:]
var cities: Set<String> = []
for line in fileContent {
    let parts = words(line)  // "London to Dublin = 464"
    let a = parts[0]
    let b = parts[2]
    distances["\(a),\(b)"] = Int(parts[4])!
    distances["\(b),\(a)"] = Int(parts[4])!
    cities.insert(a)
    cities.insert(b)
}

// Few cities, so trying every order is fast enough
let routeLengths = permutations(Array(cities)).map { route in
    (0..<(route.count - 1)).reduce(0) { $0 + distances["\(route[$1]),\(route[$1 + 1])"]! }
}

let part1Res = routeLengths.min()!
let part2Res = routeLengths.max()!

print("Part 1 res: \(part1Res)")
print("Part 2 res: \(part2Res)")
