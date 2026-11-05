import java.nio.file.*;
import java.util.*;

public class Day20 {
    static String readText(String path) throws Exception {
        return Files.readString(Path.of(path)).strip();
    }

    static List<String> readLines(String path) throws Exception {
        return readText(path).lines().toList();
    }

    public static void main(String[] args) throws Exception {
        int target = Integer.parseInt(readText(args[0]));

        int part1Res = 0;
        int part2Res = 0;

        // House n gets 10 presents from each elf that divides n, and house target / 10 + 1
        // alone gets at least target presents from its own elf, so the answer can't be further away
        int limit = target / 10 + 1;
        int[] houses = new int[limit + 1];
        for (int elf = 1; elf <= limit; elf++) {
            for (int house = elf; house <= limit; house += elf) houses[house] += elf * 10;
        }

        for (int house = 1; house <= limit; house++) {
            if (houses[house] >= target) {
                part1Res = house;
                break;
            }
        }

        // Part 2: each elf only visits 50 houses, but leaves 11 presents per house
        limit = target / 11 + 1;
        houses = new int[limit + 1];
        for (int elf = 1; elf <= limit; elf++) {
            int last = (int) Math.min((long) elf * 50, limit);
            for (int house = elf; house <= last; house += elf) houses[house] += elf * 11;
        }

        for (int house = 1; house <= limit; house++) {
            if (houses[house] >= target) {
                part2Res = house;
                break;
            }
        }

        System.out.println("Part 1 res: " + part1Res);
        System.out.println("Part 2 res: " + part2Res);
    }
}
