import java.nio.file.*;
import java.util.*;

public class Day2 {
    static String readText(String path) throws Exception {
        return Files.readString(Path.of(path)).strip();
    }

    static List<String> readLines(String path) throws Exception {
        return readText(path).lines().toList();
    }

    public static void main(String[] args) throws Exception {
        List<String> fileContent = readLines(args[0]);

        long part1Res = 0;
        long part2Res = 0;

        for (String line : fileContent) {
            String[] elem = line.split("x");
            int l = Integer.parseInt(elem[0]);
            int w = Integer.parseInt(elem[1]);
            int h = Integer.parseInt(elem[2]);

            int aSide1 = l * w;
            int aSide2 = w * h;
            int aSide3 = h * l;

            int pSide1 = 2 * l + 2 * w;
            int pSide2 = 2 * w + 2 * h;
            int pSide3 = 2 * h + 2 * l;

            part1Res += 2 * aSide1 + 2 * aSide2 + 2 * aSide3 + Math.min(aSide2, Math.min(aSide1, aSide3));
            part2Res += Math.min(pSide1, Math.min(pSide2, pSide3)) + l * w * h;
        }

        System.out.println("Part 1 res: " + part1Res);
        System.out.println("Part 2 res: " + part2Res);
    }
}
