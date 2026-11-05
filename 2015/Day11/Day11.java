import java.nio.file.*;
import java.util.*;

public class Day11 {
    static String readText(String path) throws Exception {
        return Files.readString(Path.of(path)).strip();
    }

    static List<String> readLines(String path) throws Exception {
        return readText(path).lines().toList();
    }

    static boolean increasingStraight(String string) {
        for (int i = 2; i < string.length(); i++) {
            char a = string.charAt(i), b = string.charAt(i - 1), c = string.charAt(i - 2);
            if (b == c + 1 && a == b + 1) return true;
        }
        return false;
    }

    static boolean letters(String string) {
        return string.indexOf('i') == -1 && string.indexOf('o') == -1 && string.indexOf('l') == -1;
    }

    static boolean twoGrams(String string) {
        int found = 0;
        int i = 1;
        while (i < string.length()) {
            if (string.charAt(i) == string.charAt(i - 1)) {
                found += 1;
                i += 2;  // skip so the pairs can't overlap
            } else {
                i += 1;
            }
        }
        return found >= 2;
    }

    static boolean isValid(String string) {
        return increasingStraight(string) && twoGrams(string) && letters(string);
    }

    static String increment(String string) {
        char[] chars = string.toCharArray();
        int i = chars.length - 1;
        while (i >= 0) {
            if (chars[i] == 'z') {
                chars[i] = 'a';  // wrap around and carry to the next letter on the left
                i -= 1;
            } else {
                chars[i] += 1;
                break;
            }
        }
        return new String(chars);
    }

    public static void main(String[] args) throws Exception {
        String fileContent = readText(args[0]);

        String part1Res = increment(fileContent);
        while (!isValid(part1Res)) part1Res = increment(part1Res);

        String part2Res = increment(part1Res);
        while (!isValid(part2Res)) part2Res = increment(part2Res);

        System.out.println("Part 1 res: " + part1Res);
        System.out.println("Part 2 res: " + part2Res);
    }
}
