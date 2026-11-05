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

func run(_ instructions: [[String]], _ start: [String: Int]) -> [String: Int] {
    var registers = start
    var pc = 0
    while pc >= 0 && pc < instructions.count {
        let instruction = instructions[pc]
        let action = instruction[0]
        if action == "hlf" {
            registers[instruction[1]]! /= 2
        } else if action == "tpl" {
            registers[instruction[1]]! *= 3
        } else if action == "inc" {
            registers[instruction[1]]! += 1
        } else if action == "jmp" {
            pc += Int(instruction[1])!
            continue
        } else if action == "jie" && registers[instruction[1]]! % 2 == 0 {
            pc += Int(instruction[2])!
            continue
        } else if action == "jio" && registers[instruction[1]]! == 1 {  // jump if ONE, not if odd
            pc += Int(instruction[2])!
            continue
        }
        pc += 1
    }
    return registers
}

let fileContent = readLines()

let instructions = fileContent.map { words($0.replacingOccurrences(of: ",", with: "")) }

let registers = run(instructions, ["a": 0, "b": 0])
// The puzzle's example asks for register a
let part1Res = inputPath().contains("example") ? registers["a"]! : registers["b"]!

// Part 2: same program, but register a starts at 1
let part2Res = run(instructions, ["a": 1, "b": 0])["b"]!

print("Part 1 res: \(part1Res)")
print("Part 2 res: \(part2Res)")
