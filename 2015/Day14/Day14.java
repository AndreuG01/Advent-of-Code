import java.nio.file.*;
import java.util.*;

public class Day14 {
    static String readText(String path) throws Exception {
        return Files.readString(Path.of(path)).strip();
    }

    static List<String> readLines(String path) throws Exception {
        return readText(path).lines().toList();
    }

    static class Reindeer {
        int speed, flyTime, restTime;
        int distance = 0;
        int secondsLeft;  // in the current state
        boolean flying = true;
        int points = 0;
    }

    public static void main(String[] args) throws Exception {
        List<String> fileContent = readLines(args[0]);

        List<Reindeer> results = new ArrayList<>();
        for (String line : fileContent) {
            String[] elems = line.split(" ");
            Reindeer reindeer = new Reindeer();
            reindeer.speed = Integer.parseInt(elems[3]);
            reindeer.flyTime = Integer.parseInt(elems[6]);
            reindeer.restTime = Integer.parseInt(elems[elems.length - 2]);
            reindeer.secondsLeft = reindeer.flyTime;
            results.add(reindeer);
        }

        final int N = 2503;
        int maxVal = 0;

        for (int i = 0; i < N; i++) {
            for (Reindeer reindeer : results) {
                if (reindeer.flying) reindeer.distance += reindeer.speed;
                reindeer.secondsLeft -= 1;

                if (reindeer.secondsLeft == 0) {
                    // Switch between flying and resting
                    reindeer.flying = !reindeer.flying;
                    reindeer.secondsLeft = reindeer.flying ? reindeer.flyTime : reindeer.restTime;
                }
            }
            maxVal = 0;
            for (Reindeer reindeer : results) maxVal = Math.max(maxVal, reindeer.distance);
            for (Reindeer reindeer : results) {
                if (reindeer.distance == maxVal) reindeer.points += 1;
            }
        }

        int part1Res = maxVal;
        int part2Res = 0;
        for (Reindeer reindeer : results) part2Res = Math.max(part2Res, reindeer.points);

        System.out.println("Part 1 res: " + part1Res);
        System.out.println("Part 2 res: " + part2Res);
    }
}
