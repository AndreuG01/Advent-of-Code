import java.nio.file.*;
import java.util.*;

public class Day9 {
    static String readText(String path) throws Exception {
        return Files.readString(Path.of(path)).strip();
    }

    static List<String> readLines(String path) throws Exception {
        return readText(path).lines().toList();
    }

    static List<List<String>> permutations(List<String> items) {
        if (items.size() <= 1) return List.of(items);
        List<List<String>> result = new ArrayList<>();
        for (int i = 0; i < items.size(); i++) {
            List<String> rest = new ArrayList<>(items);
            String first = rest.remove(i);
            for (List<String> order : permutations(rest)) {
                List<String> route = new ArrayList<>();
                route.add(first);
                route.addAll(order);
                result.add(route);
            }
        }
        return result;
    }

    public static void main(String[] args) throws Exception {
        List<String> fileContent = readLines(args[0]);

        // Distances work both ways, so store each pair in both directions
        Map<String, Integer> distances = new HashMap<>();
        Set<String> cities = new TreeSet<>();
        for (String line : fileContent) {
            String[] parts = line.split(" ");  // "London to Dublin = 464"
            String a = parts[0], b = parts[2];
            int dist = Integer.parseInt(parts[4]);
            distances.put(a + "," + b, dist);
            distances.put(b + "," + a, dist);
            cities.add(a);
            cities.add(b);
        }

        // Few cities, so trying every order is fast enough
        int part1Res = Integer.MAX_VALUE;
        int part2Res = 0;
        for (List<String> route : permutations(new ArrayList<>(cities))) {
            int length = 0;
            for (int i = 0; i < route.size() - 1; i++) {
                length += distances.get(route.get(i) + "," + route.get(i + 1));
            }
            part1Res = Math.min(part1Res, length);
            part2Res = Math.max(part2Res, length);
        }

        System.out.println("Part 1 res: " + part1Res);
        System.out.println("Part 2 res: " + part2Res);
    }
}
