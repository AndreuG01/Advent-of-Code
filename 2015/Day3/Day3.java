import java.nio.file.*;
import java.util.*;

public class Day3 {
    static String readText(String path) throws Exception {
        return Files.readString(Path.of(path)).strip();
    }

    static List<String> readLines(String path) throws Exception {
        return readText(path).lines().toList();
    }

    record Position(int x, int y) {
        Position moved(char elem) {
            return switch (elem) {
                case '^' -> new Position(x, y + 1);
                case '>' -> new Position(x + 1, y);
                case '<' -> new Position(x - 1, y);
                default -> new Position(x, y - 1);
            };
        }
    }

    public static void main(String[] args) throws Exception {
        String fileContent = readText(args[0]);

        Position currPos = new Position(0, 0);
        Set<Position> uniquePos = new HashSet<>(List.of(currPos));
        for (char elem : fileContent.toCharArray()) {
            currPos = currPos.moved(elem);
            uniquePos.add(currPos);
        }
        int part1Res = uniquePos.size();

        Position[] santas = {new Position(0, 0), new Position(0, 0)};  // Santa and Robo-Santa
        Set<Position> visited = new HashSet<>(List.of(new Position(0, 0)));
        for (int i = 0; i < fileContent.length(); i++) {
            santas[i % 2] = santas[i % 2].moved(fileContent.charAt(i));
            visited.add(santas[i % 2]);
        }
        int part2Res = visited.size();

        System.out.println("Part 1 res: " + part1Res);
        System.out.println("Part 2 res: " + part2Res);
    }
}
