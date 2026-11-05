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

let ON = UInt8(ascii: "#")
let OFF = UInt8(ascii: ".")

func getNeighbors(_ i: Int, _ j: Int, _ maxI: Int, _ maxJ: Int) -> [(Int, Int)] {
    var neighbors: [(Int, Int)] = []
    for a in -1...1 {
        for b in -1...1 where a != 0 || b != 0 {
            if i + a >= 0 && i + a < maxI && j + b >= 0 && j + b < maxJ {
                neighbors.append((i + a, j + b))
            }
        }
    }
    return neighbors
}

func turnOnCorners(_ grid: inout [[UInt8]]) {
    let maxI = grid.count - 1
    let maxJ = grid[0].count - 1
    for (i, j) in [(0, 0), (0, maxJ), (maxI, 0), (maxI, maxJ)] {
        grid[i][j] = ON
    }
}

func simulate(_ fileContent: [[UInt8]], _ N: Int, stuckCorners: Bool = false) -> Int {
    var grid = fileContent  // Work on a copy so each part starts from the input
    if stuckCorners { turnOnCorners(&grid) }

    for _ in 0..<N {
        var change: [(Int, Int)] = []
        for i in 0..<grid.count {
            for j in 0..<grid[i].count {
                var on = 0
                for (x, y) in getNeighbors(i, j, grid.count, grid[0].count) where grid[x][y] == ON {
                    on += 1
                }

                if grid[i][j] == ON && on != 2 && on != 3 {
                    change.append((i, j))
                } else if grid[i][j] == OFF && on == 3 {
                    change.append((i, j))
                }
            }
        }

        // All lights change at the same time, so only apply the changes after checking every light
        for (i, j) in change {
            grid[i][j] = grid[i][j] == ON ? OFF : ON
        }

        if stuckCorners { turnOnCorners(&grid) }
    }

    return grid.joined().filter { $0 == ON }.count
}

let fileContent = readLines().map { Array($0.utf8) }

let isExample = inputPath().contains("example")
let part1Res = simulate(fileContent, isExample ? 4 : 100)
let part2Res = simulate(fileContent, isExample ? 5 : 100, stuckCorners: true)

print("Part 1 res: \(part1Res)")
print("Part 2 res: \(part2Res)")
