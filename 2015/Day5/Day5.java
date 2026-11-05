import java.nio.file.*;
import java.util.*;

public class Day5 {
    static String readText(String path) throws Exception {
        return Files.readString(Path.of(path)).strip();
    }

    static List<String> readLines(String path) throws Exception {
        return readText(path).lines().toList();
    }

    static boolean threeVowels(String string) {
        return string.chars().filter(c -> "aeiou".indexOf(c) != -1).count() >= 3;
    }

    static boolean repeatedChars(String string) {
        for (int i = 1; i < string.length(); i++) {
            if (string.charAt(i) == string.charAt(i - 1)) return true;
        }
        return false;
    }

    static boolean substrings(String string) {
        for (String sub : List.of("ab", "cd", "pq", "xy")) {
            if (string.contains(sub)) return false;
        }
        return true;
    }

    static boolean twoGrams(String string) {
        Map<String, Integer> firstSeen = new HashMap<>();
        for (int i = 0; i < string.length() - 1; i++) {
            String pair = string.substring(i, i + 2);
            if (firstSeen.containsKey(pair) && i - firstSeen.get(pair) >= 2) return true;
            firstSeen.putIfAbsent(pair, i);
        }
        return false;
    }

    static boolean threeGrams(String string) {
        for (int i = 0; i < string.length() - 2; i++) {
            if (string.charAt(i) == string.charAt(i + 2)) return true;
        }
        return false;
    }

    public static void main(String[] args) throws Exception {
        List<String> fileContent = readLines(args[0]);

        int part1Res = 0;
        int part2Res = 0;

        for (String string : fileContent) {
            if (threeVowels(string) && repeatedChars(string) && substrings(string)) part1Res += 1;
            if (twoGrams(string) && threeGrams(string)) part2Res += 1;
        }

        System.out.println("Part 1 res: " + part1Res);
        System.out.println("Part 2 res: " + part2Res);
    }
}
