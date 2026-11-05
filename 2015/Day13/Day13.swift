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

// happiness["a,b"] = how much a's happiness changes when sitting next to b
var happiness: [String: Int] = [:]
var people: Set<String> = []

func totalHappiness(_ arrangement: [String]) -> Int {
    var total = 0
    for i in 0..<arrangement.count {
        let a = arrangement[i]
        let b = arrangement[(i + 1) % arrangement.count]  // the table is round
        total += happiness["\(a),\(b)"]! + happiness["\(b),\(a)"]!
    }
    return total
}

func bestArrangement(_ people: Set<String>) -> Int {
    // The table is round, so rotations are the same seating: fix the first
    // person and only try every order of the rest
    let sorted = people.sorted()
    let first = sorted[0]
    return permutations(Array(sorted.dropFirst())).map { totalHappiness([first] + $0) }.max()!
}

let fileContent = readLines()

for line in fileContent {
    // e.g. "Alice would gain 54 happiness units by sitting next to Bob."
    let parts = words(String(line.dropLast()))
    let person = parts[0]
    let neighbour = parts[parts.count - 1]
    let amount = Int(parts[3])!
    happiness["\(person),\(neighbour)"] = parts[2] == "gain" ? amount : -amount
    people.insert(person)
    people.insert(neighbour)
}

let part1Res = bestArrangement(people)

// Part 2: add yourself, with 0 happiness towards and from everyone
for person in people {
    happiness["Me,\(person)"] = 0
    happiness["\(person),Me"] = 0
}
people.insert("Me")
let part2Res = bestArrangement(people)

print("Part 1 res: \(part1Res)")
print("Part 2 res: \(part2Res)")
