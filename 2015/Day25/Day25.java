import java.nio.file.*;
import java.util.*;

public class Day25 {
    static String readText(String path) throws Exception {
        return Files.readString(Path.of(path)).strip();
    }

    static List<String> readLines(String path) throws Exception {
        return readText(path).lines().toList();
    }

    public static void main(String[] args) throws Exception {
        String fileContent = readText(args[0]);

        long[] nums = Arrays.stream(fileContent.split("[^0-9]+")).filter(part -> !part.isEmpty()).mapToLong(Long::parseLong).toArray();
        long row = nums[0], col = nums[1];

        // Codes fill the grid by diagonals: (row, col) is on diagonal row + col - 1,
        // and all the diagonals before it hold 1 + 2 + ... + (diagonal - 1) codes
        long diagonal = row + col - 1;
        long position = diagonal * (diagonal - 1) / 2 + col;

        long code = 20151125;
        for (long i = 0; i < position - 1; i++) code = code * 252533 % 33554393;

        long part1Res = code;
        long part2Res = 0;

        System.out.println("Part 1 res: " + part1Res);
        System.out.println("Part 2 res: " + part2Res);
    }
}
