import java.nio.file.*;
import java.util.*;

public class Day13 {
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

    // happiness["a,b"] = how much a's happiness changes when sitting next to b
    static Map<String, Integer> happiness = new HashMap<>();

    static int totalHappiness(List<String> arrangement) {
        int total = 0;
        for (int i = 0; i < arrangement.size(); i++) {
            String a = arrangement.get(i);
            String b = arrangement.get((i + 1) % arrangement.size());  // the table is round
            total += happiness.get(a + "," + b) + happiness.get(b + "," + a);
        }
        return total;
    }

    static int bestArrangement(Set<String> people) {
        // The table is round, so rotations are the same seating: fix the first
        // person and only try every order of the rest
        List<String> sorted = new ArrayList<>(new TreeSet<>(people));
        String first = sorted.remove(0);
        int best = Integer.MIN_VALUE;
        for (List<String> order : permutations(sorted)) {
            List<String> arrangement = new ArrayList<>(order);
            arrangement.add(0, first);
            best = Math.max(best, totalHappiness(arrangement));
        }
        return best;
    }

    public static void main(String[] args) throws Exception {
        List<String> fileContent = readLines(args[0]);

        Set<String> people = new HashSet<>();
        for (String line : fileContent) {
            // e.g. "Alice would gain 54 happiness units by sitting next to Bob."
            String[] words = line.substring(0, line.length() - 1).split(" ");
            String person = words[0];
            String neighbour = words[words.length - 1];
            int amount = Integer.parseInt(words[3]);
            happiness.put(person + "," + neighbour, words[2].equals("gain") ? amount : -amount);
            people.add(person);
            people.add(neighbour);
        }

        int part1Res = bestArrangement(people);

        // Part 2: add yourself, with 0 happiness towards and from everyone
        for (String person : people) {
            happiness.put("Me," + person, 0);
            happiness.put(person + ",Me", 0);
        }
        people.add("Me");
        int part2Res = bestArrangement(people);

        System.out.println("Part 1 res: " + part1Res);
        System.out.println("Part 2 res: " + part2Res);
    }
}
