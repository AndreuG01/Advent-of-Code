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

func sumNumbers(_ obj: Any, ignoreRed: Bool = false) -> Int {
    // Walk the JSON recursively and add up every number found
    if obj is String { return 0 }
    if let number = obj as? Int { return number }
    if let list = obj as? [Any] {
        return list.reduce(0) { $0 + sumNumbers($1, ignoreRed: ignoreRed) }
    }
    if let dict = obj as? [String: Any] {
        // Part 2: skip any object (not array) that has "red" as a value
        if ignoreRed && dict.values.contains(where: { ($0 as? String) == "red" }) { return 0 }
        return dict.values.reduce(0) { $0 + sumNumbers($1, ignoreRed: ignoreRed) }
    }
    return 0
}

let fileContent = readText()

let jsonObj = try! JSONSerialization.jsonObject(with: Data(fileContent.utf8), options: [.fragmentsAllowed])

let part1Res = sumNumbers(jsonObj)
let part2Res = sumNumbers(jsonObj, ignoreRed: true)

print("Part 1 res: \(part1Res)")
print("Part 2 res: \(part2Res)")
