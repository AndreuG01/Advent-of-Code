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

func fewestSteps(_ molecule: String, _ replacements: [(String, String)]) -> Int {
    // Work backwards from the molecule to "e". Every way down takes the same number
    // of steps, but a greedy path can get stuck, so restart with a new order if it does
    var rules = replacements
    while true {
        rules.shuffle()
        var curr = molecule
        var steps = 0
        var changed = true
        while curr != "e" && changed {
            changed = false
            for (source, target) in rules {
                if let range = curr.range(of: target) {
                    curr.replaceSubrange(range, with: source)
                    steps += 1
                    changed = true
                    break
                }
            }
        }
        if curr == "e" { return steps }
    }
}

let fileContent = readText()

let sections = fileContent.components(separatedBy: "\n\n")
let molecule = sections[1]
let replacements = sections[0].split(separator: "\n").map { line -> (String, String) in
    let parts = line.components(separatedBy: " => ")
    return (parts[0], parts[1])
}

var molecules: Set<String> = []
for (source, target) in replacements {
    var searchStart = molecule.startIndex
    while let range = molecule.range(of: source, range: searchStart..<molecule.endIndex) {
        molecules.insert(molecule.replacingCharacters(in: range, with: target))
        searchStart = molecule.index(after: range.lowerBound)
    }
}

let part1Res = molecules.count
let part2Res = fewestSteps(molecule, replacements)

print("Part 1 res: \(part1Res)")
print("Part 2 res: \(part2Res)")
