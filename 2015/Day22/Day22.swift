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

struct State: Hashable {
    var spent: Int
    var hp: Int
    var mana: Int
    var boss: Int
    var shield = 0
    var poison = 0
    var recharge = 0

    mutating func applyEffects() -> Int {
        let armor = shield > 0 ? 7 : 0
        if poison > 0 { boss -= 3 }
        if recharge > 0 { mana += 101 }
        shield = max(shield - 1, 0)
        poison = max(poison - 1, 0)
        recharge = max(recharge - 1, 0)
        return armor
    }
}

// Swift has no priority queue in its standard library, so here is a small binary heap
struct Heap {
    var items: [State] = []

    mutating func push(_ state: State) {
        items.append(state)
        var i = items.count - 1
        while i > 0 && items[i].spent < items[(i - 1) / 2].spent {
            items.swapAt(i, (i - 1) / 2)
            i = (i - 1) / 2
        }
    }

    mutating func pop() -> State? {
        if items.isEmpty { return nil }
        items.swapAt(0, items.count - 1)
        let top = items.removeLast()
        var i = 0
        while true {
            var smallest = i
            for child in [2 * i + 1, 2 * i + 2] where child < items.count && items[child].spent < items[smallest].spent {
                smallest = child
            }
            if smallest == i { break }
            items.swapAt(i, smallest)
            i = smallest
        }
        return top
    }
}

func castSpells(_ state: State) -> [State] {
    // Every spell that can be cast now, with its cost added to spent and taken from mana
    func paying(_ cost: Int, _ change: (inout State) -> Void) -> State {
        var next = state
        next.spent += cost
        next.mana -= cost
        change(&next)
        return next
    }

    var options = [
        (53, paying(53) { $0.boss -= 4 }),  // Magic Missile
        (73, paying(73) { $0.boss -= 2; $0.hp += 2 }),  // Drain
    ]
    if state.shield == 0 { options.append((113, paying(113) { $0.shield = 6 })) }
    if state.poison == 0 { options.append((173, paying(173) { $0.poison = 6 })) }
    if state.recharge == 0 { options.append((229, paying(229) { $0.recharge = 5 })) }
    return options.filter { $0.0 <= state.mana }.map { $0.1 }
}

func leastMana(_ playerHp: Int, _ playerMana: Int, _ bossHp: Int, _ bossDamage: Int, hard: Bool = false) -> Int? {
    // Dijkstra: always continue from the fight that has spent the least mana so far,
    // so the first won fight taken from the queue is the cheapest one
    var queue = Heap()
    queue.push(State(spent: 0, hp: playerHp, mana: playerMana, boss: bossHp))
    var seen: Set<State> = []

    while var state = queue.pop() {
        if state.boss <= 0 { return state.spent }
        if !seen.insert(state).inserted { continue }

        // Player turn
        if hard {
            // Part 2: lose 1 HP at the start of each player turn, before effects
            state.hp -= 1
            if state.hp <= 0 { continue }
        }

        _ = state.applyEffects()
        if state.boss <= 0 {
            queue.push(state)
            continue
        }

        for var next in castSpells(state) {
            // Boss turn
            let armor = next.applyEffects()
            if next.boss > 0 {
                next.hp -= max(1, bossDamage - armor)
                if next.hp <= 0 { continue }
            }
            queue.push(next)
        }
    }
    return nil  // the fight can't be won
}

func show(_ mana: Int?) -> String {
    return mana.map { String($0) } ?? "None"
}

let fileContent = readLines()

let boss = fileContent.map { Int($0.components(separatedBy: ": ")[1])! }

// The puzzle's examples use a weaker player
let isExample = inputPath().contains("example")
let playerHp = isExample ? 10 : 50
let playerMana = isExample ? 250 : 500

let part1Res = show(leastMana(playerHp, playerMana, boss[0], boss[1]))
let part2Res = show(leastMana(playerHp, playerMana, boss[0], boss[1], hard: true))

print("Part 1 res: \(part1Res)")
print("Part 2 res: \(part2Res)")
