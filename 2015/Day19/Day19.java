import java.nio.file.*;
import java.util.*;

public class Day19 {
    static String readText(String path) throws Exception {
        return Files.readString(Path.of(path)).strip();
    }

    static List<String> readLines(String path) throws Exception {
        return readText(path).lines().toList();
    }

    static int fewestSteps(String molecule, List<String[]> replacements) {
        // Work backwards from the molecule to "e". Every way down takes the same number
        // of steps, but a greedy path can get stuck, so restart with a new order if it does
        List<String[]> rules = new ArrayList<>(replacements);
        while (true) {
            Collections.shuffle(rules);
            String curr = molecule;
            int steps = 0;
            boolean changed = true;
            while (!curr.equals("e") && changed) {
                changed = false;
                for (String[] rule : rules) {
                    int i = curr.indexOf(rule[1]);
                    if (i != -1) {
                        curr = curr.substring(0, i) + rule[0] + curr.substring(i + rule[1].length());
                        steps += 1;
                        changed = true;
                        break;
                    }
                }
            }
            if (curr.equals("e")) return steps;
        }
    }

    public static void main(String[] args) throws Exception {
        String fileContent = readText(args[0]);

        String[] sections = fileContent.split("\n\n");
        String molecule = sections[1];
        List<String[]> replacements = new ArrayList<>();
        for (String line : sections[0].split("\n")) replacements.add(line.split(" => "));

        Set<String> molecules = new HashSet<>();
        for (String[] rule : replacements) {
            String source = rule[0], target = rule[1];
            int i = molecule.indexOf(source);
            while (i != -1) {
                molecules.add(molecule.substring(0, i) + target + molecule.substring(i + source.length()));
                i = molecule.indexOf(source, i + 1);
            }
        }

        int part1Res = molecules.size();
        int part2Res = fewestSteps(molecule, replacements);

        System.out.println("Part 1 res: " + part1Res);
        System.out.println("Part 2 res: " + part2Res);
    }
}
