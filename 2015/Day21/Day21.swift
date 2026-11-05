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

typealias Item = (cost: Int, damage: Int, armor: Int)

let weapons: [Item] = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
let armors: [Item] = [(13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)]
let rings: [Item] = [(25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)]

func playerWins(_ playerStart: Int, _ playerDamage: Int, _ playerArmor: Int, _ bossStart: Int, _ bossDamage: Int, _ bossArmor: Int) -> Bool {
    var playerHp = playerStart
    var bossHp = bossStart
    while true {
        bossHp -= max(1, playerDamage - bossArmor)
        if bossHp <= 0 { return true }
        playerHp -= max(1, bossDamage - playerArmor)
        if playerHp <= 0 { return false }
    }
}

func loadouts() -> [[Item]] {
    // Exactly 1 weapon, 0 or 1 armor, 0 to 2 rings
    let armorOptions: [[Item]] = [[]] + armors.map { [$0] }
    var ringOptions: [[Item]] = [[]]
    for i in 0..<rings.count {
        ringOptions.append([rings[i]])
        for j in (i + 1)..<rings.count {
            ringOptions.append([rings[i], rings[j]])
        }
    }

    var result: [[Item]] = []
    for weapon in weapons {
        for armor in armorOptions {
            for ring in ringOptions {
                result.append([weapon] + armor + ring)
            }
        }
    }
    return result
}

let fileContent = readLines()

let boss = fileContent.map { Int($0.components(separatedBy: ": ")[1])! }

var part1Res = Int.max
var part2Res = 0

for items in loadouts() {
    let cost = items.reduce(0) { $0 + $1.cost }
    let damage = items.reduce(0) { $0 + $1.damage }
    let armor = items.reduce(0) { $0 + $1.armor }
    if playerWins(100, damage, armor, boss[0], boss[1], boss[2]) {
        part1Res = min(part1Res, cost)
    } else {
        part2Res = max(part2Res, cost)
    }
}

print("Part 1 res: \(part1Res)")
print("Part 2 res: \(part2Res)")
