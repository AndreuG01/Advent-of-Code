import java.nio.file.*;
import java.util.*;

public class Day21 {
    static String readText(String path) throws Exception {
        return Files.readString(Path.of(path)).strip();
    }

    static List<String> readLines(String path) throws Exception {
        return readText(path).lines().toList();
    }

    record Item(int cost, int damage, int armor) {}

    static final List<Item> WEAPONS = List.of(new Item(8, 4, 0), new Item(10, 5, 0), new Item(25, 6, 0), new Item(40, 7, 0), new Item(74, 8, 0));
    static final List<Item> ARMORS = List.of(new Item(13, 0, 1), new Item(31, 0, 2), new Item(53, 0, 3), new Item(75, 0, 4), new Item(102, 0, 5));
    static final List<Item> RINGS = List.of(new Item(25, 1, 0), new Item(50, 2, 0), new Item(100, 3, 0), new Item(20, 0, 1), new Item(40, 0, 2), new Item(80, 0, 3));

    static boolean playerWins(int playerHp, int playerDamage, int playerArmor, int bossHp, int bossDamage, int bossArmor) {
        while (true) {
            bossHp -= Math.max(1, playerDamage - bossArmor);
            if (bossHp <= 0) return true;
            playerHp -= Math.max(1, bossDamage - playerArmor);
            if (playerHp <= 0) return false;
        }
    }

    static List<List<Item>> loadouts() {
        // Exactly 1 weapon, 0 or 1 armor, 0 to 2 rings
        List<List<Item>> armorOptions = new ArrayList<>();
        armorOptions.add(List.of());
        for (Item armor : ARMORS) armorOptions.add(List.of(armor));

        List<List<Item>> ringOptions = new ArrayList<>();
        ringOptions.add(List.of());
        for (int i = 0; i < RINGS.size(); i++) {
            ringOptions.add(List.of(RINGS.get(i)));
            for (int j = i + 1; j < RINGS.size(); j++) ringOptions.add(List.of(RINGS.get(i), RINGS.get(j)));
        }

        List<List<Item>> result = new ArrayList<>();
        for (Item weapon : WEAPONS) {
            for (List<Item> armor : armorOptions) {
                for (List<Item> ring : ringOptions) {
                    List<Item> items = new ArrayList<>();
                    items.add(weapon);
                    items.addAll(armor);
                    items.addAll(ring);
                    result.add(items);
                }
            }
        }
        return result;
    }

    public static void main(String[] args) throws Exception {
        List<String> fileContent = readLines(args[0]);

        int[] boss = fileContent.stream().mapToInt(line -> Integer.parseInt(line.split(": ")[1])).toArray();

        int part1Res = Integer.MAX_VALUE;
        int part2Res = 0;

        for (List<Item> items : loadouts()) {
            int cost = items.stream().mapToInt(Item::cost).sum();
            int damage = items.stream().mapToInt(Item::damage).sum();
            int armor = items.stream().mapToInt(Item::armor).sum();
            if (playerWins(100, damage, armor, boss[0], boss[1], boss[2])) part1Res = Math.min(part1Res, cost);
            else part2Res = Math.max(part2Res, cost);
        }

        System.out.println("Part 1 res: " + part1Res);
        System.out.println("Part 2 res: " + part2Res);
    }
}
