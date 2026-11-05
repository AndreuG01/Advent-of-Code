import java.nio.file.*;
import java.util.*;

public class Day16 {
    static String readText(String path) throws Exception {
        return Files.readString(Path.of(path)).strip();
    }

    static List<String> readLines(String path) throws Exception {
        return readText(path).lines().toList();
    }

    public static void main(String[] args) throws Exception {
        List<String> fileContent = readLines(args[0]);

        int part1Res = 0;
        int part2Res = 0;

        Map<String, Integer> target = Map.of(
            "children", 3, "cats", 7, "samoyeds", 2, "pomeranians", 3, "akitas", 0,
            "vizslas", 0, "goldfish", 5, "trees", 3, "cars", 2, "perfumes", 1
        );

        for (int i = 0; i < fileContent.size(); i++) {
            String[] parts = fileContent.get(i).replace(":", "").replace(",", "").split(" ");

            boolean matches = true;
            boolean matches2 = true;
            for (int idx = 2; idx < parts.length; idx += 2) {
                String detect = parts[idx];
                int val = Integer.parseInt(parts[idx + 1]);
                int expected = target.get(detect);
                if (expected != val) matches = false;

                // Part 2: cats and trees are lower bounds, pomeranians and goldfish upper bounds
                if (detect.equals("cats") || detect.equals("trees")) {
                    if (val <= expected) matches2 = false;
                } else if (detect.equals("pomeranians") || detect.equals("goldfish")) {
                    if (val >= expected) matches2 = false;
                } else if (expected != val) {
                    matches2 = false;
                }
            }
            if (matches) part1Res = i + 1;
            if (matches2) part2Res = i + 1;
        }

        System.out.println("Part 1 res: " + part1Res);
        System.out.println("Part 2 res: " + part2Res);
    }
}
