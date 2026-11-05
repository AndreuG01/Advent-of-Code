import java.nio.file.*;
import java.util.*;

public class Day24 {
    static String readText(String path) throws Exception {
        return Files.readString(Path.of(path)).strip();
    }

    static List<String> readLines(String path) throws Exception {
        return readText(path).lines().toList();
    }

    static long prod(List<Long> group) {
        long result = 1;
        for (long weight : group) result *= weight;
        return result;
    }

    static long sum(List<Long> group) {
        long result = 0;
        for (long weight : group) result += weight;
        return result;
    }

    static List<Long> without(List<Long> weights, List<Long> group) {
        List<Long> rest = new ArrayList<>(weights);
        for (Long weight : group) rest.remove(weight);
        return rest;
    }

    // All groups of exactly size packages that add up to target
    static void combinations(List<Long> weights, int start, int size, long target, List<Long> curr, List<List<Long>> groups) {
        if (size == 0) {
            if (target == 0) groups.add(new ArrayList<>(curr));
            return;
        }
        for (int i = start; i < weights.size(); i++) {
            if (weights.get(i) > target) continue;
            curr.add(weights.get(i));
            combinations(weights, i + 1, size - 1, target - weights.get(i), curr, groups);
            curr.remove(curr.size() - 1);
        }
    }

    static List<List<Long>> groupsOfSize(List<Long> weights, int size, long target) {
        List<List<Long>> groups = new ArrayList<>();
        combinations(weights, 0, size, target, new ArrayList<>(), groups);
        return groups;
    }

    static boolean canSplit(List<Long> weights, int numGroups, long target) {
        if (numGroups == 1) return sum(weights) == target;
        for (int size = 1; size <= weights.size(); size++) {
            for (List<Long> group : groupsOfSize(weights, size, target)) {
                if (canSplit(without(weights, group), numGroups - 1, target)) return true;
            }
        }
        return false;
    }

    static long bestEntanglement(List<Long> weights, int numGroups) {
        long target = sum(weights) / numGroups;
        // Sizes go up, so the first size with a valid group has the fewest packages
        for (int size = 1; size <= weights.size(); size++) {
            List<List<Long>> groups = groupsOfSize(weights, size, target);
            groups.sort(Comparator.comparingLong(Day24::prod));
            for (List<Long> group : groups) {
                // The rest of the packages also have to split into equal groups
                if (canSplit(without(weights, group), numGroups - 1, target)) return prod(group);
            }
        }
        throw new IllegalStateException("No valid split");
    }

    public static void main(String[] args) throws Exception {
        List<String> fileContent = readLines(args[0]);

        List<Long> weights = new ArrayList<>();
        for (String line : fileContent) weights.add(Long.parseLong(line));

        long part1Res = bestEntanglement(weights, 3);
        long part2Res = bestEntanglement(weights, 4);

        System.out.println("Part 1 res: " + part1Res);
        System.out.println("Part 2 res: " + part2Res);
    }
}
