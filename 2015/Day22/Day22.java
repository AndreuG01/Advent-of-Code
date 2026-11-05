import java.nio.file.*;
import java.util.*;

public class Day22 {
    static String readText(String path) throws Exception {
        return Files.readString(Path.of(path)).strip();
    }

    static List<String> readLines(String path) throws Exception {
        return readText(path).lines().toList();
    }

    record State(int spent, int hp, int mana, int boss, int shield, int poison, int recharge) {
        // Effects at the start of a turn
        State applyEffects() {
            return new State(
                spent, hp,
                recharge > 0 ? mana + 101 : mana,
                poison > 0 ? boss - 3 : boss,
                Math.max(shield - 1, 0), Math.max(poison - 1, 0), Math.max(recharge - 1, 0)
            );
        }

        // Every spell that can be cast now
        List<State> castSpells() {
            List<State> options = new ArrayList<>();
            if (mana >= 53) options.add(new State(spent + 53, hp, mana - 53, boss - 4, shield, poison, recharge));  // Magic Missile
            if (mana >= 73) options.add(new State(spent + 73, hp + 2, mana - 73, boss - 2, shield, poison, recharge));  // Drain
            if (mana >= 113 && shield == 0) options.add(new State(spent + 113, hp, mana - 113, boss, 6, poison, recharge));
            if (mana >= 173 && poison == 0) options.add(new State(spent + 173, hp, mana - 173, boss, shield, 6, recharge));
            if (mana >= 229 && recharge == 0) options.add(new State(spent + 229, hp, mana - 229, boss, shield, poison, 5));
            return options;
        }
    }

    static Integer leastMana(int playerHp, int playerMana, int bossHp, int bossDamage, boolean hard) {
        // Dijkstra: always continue from the fight that has spent the least mana so far,
        // so the first won fight taken from the queue is the cheapest one
        PriorityQueue<State> queue = new PriorityQueue<>(Comparator.comparingInt(State::spent));
        queue.add(new State(0, playerHp, playerMana, bossHp, 0, 0, 0));
        Set<State> seen = new HashSet<>();

        while (!queue.isEmpty()) {
            State state = queue.poll();
            if (state.boss() <= 0) return state.spent();
            if (!seen.add(state)) continue;

            // Player turn
            if (hard) {
                // Part 2: lose 1 HP at the start of each player turn, before effects
                state = new State(state.spent(), state.hp() - 1, state.mana(), state.boss(), state.shield(), state.poison(), state.recharge());
                if (state.hp() <= 0) continue;
            }

            state = state.applyEffects();
            if (state.boss() <= 0) {
                queue.add(state);
                continue;
            }

            for (State spell : state.castSpells()) {
                // Boss turn
                int armor = spell.shield() > 0 ? 7 : 0;
                State next = spell.applyEffects();
                int hp = next.hp();
                if (next.boss() > 0) {
                    hp -= Math.max(1, bossDamage - armor);
                    if (hp <= 0) continue;
                }
                queue.add(new State(next.spent(), hp, next.mana(), next.boss(), next.shield(), next.poison(), next.recharge()));
            }
        }
        return null;  // the fight can't be won
    }

    static String show(Integer mana) {
        return mana == null ? "None" : mana.toString();
    }

    public static void main(String[] args) throws Exception {
        List<String> fileContent = readLines(args[0]);

        int[] boss = fileContent.stream().mapToInt(line -> Integer.parseInt(line.split(": ")[1])).toArray();

        // The puzzle's examples use a weaker player
        boolean isExample = args[0].contains("example");
        int playerHp = isExample ? 10 : 50;
        int playerMana = isExample ? 250 : 500;

        String part1Res = show(leastMana(playerHp, playerMana, boss[0], boss[1], false));
        String part2Res = show(leastMana(playerHp, playerMana, boss[0], boss[1], true));

        System.out.println("Part 1 res: " + part1Res);
        System.out.println("Part 2 res: " + part2Res);
    }
}
