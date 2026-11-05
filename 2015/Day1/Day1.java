import java.nio.file.*;
import java.util.*;

public class Day1 {
    static String readText(String path) throws Exception {
        return Files.readString(Path.of(path)).strip();
    }

    static List<String> readLines(String path) throws Exception {
        return readText(path).lines().toList();
    }

    public static void main(String[] args) throws Exception {
        String fileContent = readText(args[0]);

        int part1Res = 0;
        int part2Res = 0;
        boolean part2Done = false;

        for (int i = 0; i < fileContent.length(); i++) {
            if (fileContent.charAt(i) == '(') part1Res += 1;
            else part1Res -= 1;
            if (part1Res == -1 && !part2Done) {
                part2Res = i + 1;
                part2Done = true;
            }
        }

        System.out.println("Part 1 res: " + part1Res);
        System.out.println("Part 2 res: " + part2Res);
    }
}
