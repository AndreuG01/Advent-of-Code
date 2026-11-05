import java.nio.file.*;
import java.util.*;

public class Day17 {
    static String readText(String path) throws Exception {
        return Files.readString(Path.of(path)).strip();
    }

    static List<String> readLines(String path) throws Exception {
        return readText(path).lines().toList();
    }

    public static void main(String[] args) throws Exception {
        String fileContent = readText(args[0]);

        int[] nums = Arrays.stream(fileContent.split("\\s+")).mapToInt(Integer::parseInt).toArray();

        int part1Res = 0;
        int part2Res = 0;

        int target = args[0].contains("example") ? 25 : 150;

        // Each bit of mask says if a container is used, so same-size containers stay different.
        // ways[size] counts the matching groups with that many containers.
        int[] ways = new int[nums.length + 1];
        for (int mask = 1; mask < (1 << nums.length); mask++) {
            int total = 0;
            for (int i = 0; i < nums.length; i++) {
                if ((mask & (1 << i)) != 0) total += nums[i];
            }
            if (total == target) ways[Integer.bitCount(mask)] += 1;
        }

        for (int currRes : ways) {
            part1Res += currRes;
            // Part 2: sizes go up, so the first size with a match is the minimum
            if (part2Res == 0) part2Res = currRes;
        }

        System.out.println("Part 1 res: " + part1Res);
        System.out.println("Part 2 res: " + part2Res);
    }
}
