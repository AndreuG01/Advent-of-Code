import java.nio.file.*;
import java.util.*;

public class Day10 {
    static String readText(String path) throws Exception {
        return Files.readString(Path.of(path)).strip();
    }

    static List<String> readLines(String path) throws Exception {
        return readText(path).lines().toList();
    }

    static String lookAndSay(String s) {
        int count = 1;
        char val = s.charAt(0);
        StringBuilder newStr = new StringBuilder();
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == val) {
                count += 1;
            } else {
                newStr.append(count).append(val);
                count = 1;
            }
            val = s.charAt(i);
        }
        newStr.append(count).append(val);
        return newStr.toString();
    }

    public static void main(String[] args) throws Exception {
        String seq = readText(args[0]);

        int part1Res = 0;

        for (int i = 0; i < 50; i++) {
            seq = lookAndSay(seq);
            if (i == 39) part1Res = seq.length();
        }
        int part2Res = seq.length();

        System.out.println("Part 1 res: " + part1Res);
        System.out.println("Part 2 res: " + part2Res);
    }
}
