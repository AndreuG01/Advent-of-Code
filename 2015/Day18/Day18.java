import java.nio.file.*;
import java.util.*;

public class Day18 {
    static String readText(String path) throws Exception {
        return Files.readString(Path.of(path)).strip();
    }

    static List<String> readLines(String path) throws Exception {
        return readText(path).lines().toList();
    }

    static List<int[]> getNeighbors(int i, int j, int maxI, int maxJ) {
        List<int[]> neighbors = new ArrayList<>();
        for (int a = -1; a <= 1; a++) {
            for (int b = -1; b <= 1; b++) {
                if (a == 0 && b == 0) continue;
                if (i + a >= 0 && i + a < maxI && j + b >= 0 && j + b < maxJ) neighbors.add(new int[] {i + a, j + b});
            }
        }
        return neighbors;
    }

    static void turnOnCorners(char[][] grid) {
        int maxI = grid.length - 1, maxJ = grid[0].length - 1;
        grid[0][0] = grid[0][maxJ] = grid[maxI][0] = grid[maxI][maxJ] = '#';
    }

    static int simulate(List<String> fileContent, int N, boolean stuckCorners) {
        // Work on a copy so each part starts from the input
        char[][] grid = new char[fileContent.size()][];
        for (int i = 0; i < grid.length; i++) grid[i] = fileContent.get(i).toCharArray();
        if (stuckCorners) turnOnCorners(grid);

        for (int turn = 0; turn < N; turn++) {
            List<int[]> change = new ArrayList<>();
            for (int i = 0; i < grid.length; i++) {
                for (int j = 0; j < grid[i].length; j++) {
                    int on = 0;
                    for (int[] n : getNeighbors(i, j, grid.length, grid[0].length)) {
                        if (grid[n[0]][n[1]] == '#') on += 1;
                    }

                    if (grid[i][j] == '#' && on != 2 && on != 3) change.add(new int[] {i, j});
                    else if (grid[i][j] == '.' && on == 3) change.add(new int[] {i, j});
                }
            }

            // All lights change at the same time, so only apply the changes after checking every light
            for (int[] light : change) {
                grid[light[0]][light[1]] = grid[light[0]][light[1]] == '#' ? '.' : '#';
            }

            if (stuckCorners) turnOnCorners(grid);
        }

        int total = 0;
        for (char[] row : grid) {
            for (char light : row) {
                if (light == '#') total += 1;
            }
        }
        return total;
    }

    public static void main(String[] args) throws Exception {
        List<String> fileContent = readLines(args[0]);

        boolean isExample = args[0].contains("example");
        int part1Res = simulate(fileContent, isExample ? 4 : 100, false);
        int part2Res = simulate(fileContent, isExample ? 5 : 100, true);

        System.out.println("Part 1 res: " + part1Res);
        System.out.println("Part 2 res: " + part2Res);
    }
}
