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

let MASK = 0xFFFF  // signals are 16-bit

// Instructions are not in order, so first store how each wire is computed,
// then resolve wires recursively (memoized) when asked for
var circuit: [String: [String]] = [:]
var cache: [String: Int] = [:]

func signal(_ name: String) -> Int {
    if let number = Int(name) { return number }
    if let cached = cache[name] { return cached }

    let operation = circuit[name]!
    var result: Int
    if operation.count == 1 {
        // e.g. "123 -> x" or "lx -> a"
        result = signal(operation[0])
    } else if operation.count == 2 {
        // NOT x
        result = ~signal(operation[1]) & MASK
    } else {
        let one = signal(operation[0])
        let two = signal(operation[2])
        switch operation[1] {
        case "AND": result = one & two
        case "OR": result = one | two
        case "LSHIFT": result = (one << two) & MASK
        case "RSHIFT": result = one >> two
        default: fatalError("Unknown action: \(operation[1])")
        }
    }
    cache[name] = result
    return result
}

let fileContent = readLines()

var part1Res = 0
var part2Res = 0

for line in fileContent {
    let split = line.components(separatedBy: " -> ")
    circuit[split[1]] = words(split[0])
}

if circuit["a"] != nil {
    part1Res = signal("a")

    // Part 2: override wire b with part 1's signal, reset all wires and rerun
    circuit["b"] = [String(part1Res)]
    cache = [:]
    part2Res = signal("a")
} else {
    // The example has no wire "a": show every wire instead
    for wire in circuit.keys.sorted() {
        print("\(wire): \(signal(wire))")
    }
}

print("Part 1 res: \(part1Res)")
print("Part 2 res: \(part2Res)")
