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

func prod(_ group: [Int]) -> Int {
    return group.reduce(1, *)
}

func without(_ weights: [Int], _ group: [Int]) -> [Int] {
    var rest = weights
    for weight in group {
        rest.remove(at: rest.firstIndex(of: weight)!)
    }
    return rest
}

// All groups of exactly size packages that add up to target
func combinations(_ weights: [Int], _ start: Int, _ size: Int, _ target: Int, _ curr: inout [Int], _ groups: inout [[Int]]) {
    if size == 0 {
        if target == 0 { groups.append(curr) }
        return
    }
    for i in start..<weights.count where weights[i] <= target {
        curr.append(weights[i])
        combinations(weights, i + 1, size - 1, target - weights[i], &curr, &groups)
        curr.removeLast()
    }
}

func groupsOfSize(_ weights: [Int], _ size: Int, _ target: Int) -> [[Int]] {
    var groups: [[Int]] = []
    var curr: [Int] = []
    combinations(weights, 0, size, target, &curr, &groups)
    return groups
}

func canSplit(_ weights: [Int], _ numGroups: Int, _ target: Int) -> Bool {
    if numGroups == 1 { return weights.reduce(0, +) == target }
    for size in 1...weights.count {
        for group in groupsOfSize(weights, size, target) {
            if canSplit(without(weights, group), numGroups - 1, target) { return true }
        }
    }
    return false
}

func bestEntanglement(_ weights: [Int], _ numGroups: Int) -> Int {
    let target = weights.reduce(0, +) / numGroups
    // Sizes go up, so the first size with a valid group has the fewest packages
    for size in 1...weights.count {
        let groups = groupsOfSize(weights, size, target).sorted { prod($0) < prod($1) }
        for group in groups {
            // The rest of the packages also have to split into equal groups
            if canSplit(without(weights, group), numGroups - 1, target) { return prod(group) }
        }
    }
    fatalError("No valid split")
}

let fileContent = readLines()

let weights = fileContent.map { Int($0)! }

let part1Res = bestEntanglement(weights, 3)
let part2Res = bestEntanglement(weights, 4)

print("Part 1 res: \(part1Res)")
print("Part 2 res: \(part2Res)")
