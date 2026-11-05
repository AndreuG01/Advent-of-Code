import java.nio.file.*;
import java.util.*;

public class Day6 {
    static String readText(String path) throws Exception {
        return Files.readString(Path.of(path)).strip();
    }

    static List<String> readLines(String path) throws Exception {
        return readText(path).lines().toList();
    }

    public static void main(String[] args) throws Exception {
        List<String> fileContent = readLines(args[0]);

        int[][] points = new int[1000][1000];
        int[][] points2 = new int[1000][1000];

        for (String line : fileContent) {
            String[] elems = line.split(" ");
            // "toggle a,b through c,d" has 4 words, "turn on a,b through c,d" has 5
            String action = elems.length == 4 ? "toggle" : elems[1];
            String[] numsF = elems[elems.length - 3].split(",");
            String[] numsT = elems[elems.length - 1].split(",");
            int fX = Integer.parseInt(numsF[0]), fY = Integer.parseInt(numsF[1]);
            int tX = Integer.parseInt(numsT[0]), tY = Integer.parseInt(numsT[1]);

            for (int x = fX; x <= tX; x++) {
                for (int y = fY; y <= tY; y++) {
                    if (action.equals("off")) {
                        points[x][y] = 0;
                        points2[x][y] = Math.max(0, points2[x][y] - 1);
                    } else if (action.equals("on")) {
                        points[x][y] = 1;
                        points2[x][y] += 1;
                    } else {
                        points[x][y] = 1 - points[x][y];
                        points2[x][y] += 2;
                    }
                }
            }
        }

        long part1Res = 0;
        long part2Res = 0;
        for (int x = 0; x < 1000; x++) {
            for (int y = 0; y < 1000; y++) {
                part1Res += points[x][y];
                part2Res += points2[x][y];
            }
        }

        System.out.println("Part 1 res: " + part1Res);
        System.out.println("Part 2 res: " + part2Res);
    }
}
