import java.nio.file.*;
import java.util.*;

public class Day7 {
    static String readText(String path) throws Exception {
        return Files.readString(Path.of(path)).strip();
    }

    static List<String> readLines(String path) throws Exception {
        return readText(path).lines().toList();
    }

    static final int MASK = 0xFFFF;  // signals are 16-bit

    // Instructions are not in order, so first store how each wire is computed,
    // then resolve wires recursively (memoized) when asked for
    static Map<String, String[]> circuit = new TreeMap<>();
    static Map<String, Integer> cache = new HashMap<>();

    static int signal(String name) {
        if (Character.isDigit(name.charAt(0))) return Integer.parseInt(name);
        if (cache.containsKey(name)) return cache.get(name);

        String[] operation = circuit.get(name);
        int result;
        if (operation.length == 1) {
            // e.g. "123 -> x" or "lx -> a"
            result = signal(operation[0]);
        } else if (operation.length == 2) {
            // NOT x
            result = ~signal(operation[1]) & MASK;
        } else {
            int one = signal(operation[0]);
            int two = signal(operation[2]);
            result = switch (operation[1]) {
                case "AND" -> one & two;
                case "OR" -> one | two;
                case "LSHIFT" -> (one << two) & MASK;
                case "RSHIFT" -> one >> two;
                default -> throw new IllegalArgumentException("Unknown action: " + operation[1]);
            };
        }
        cache.put(name, result);
        return result;
    }

    public static void main(String[] args) throws Exception {
        List<String> fileContent = readLines(args[0]);

        int part1Res = 0;
        int part2Res = 0;

        for (String line : fileContent) {
            String[] split = line.split(" -> ");
            circuit.put(split[1], split[0].split(" "));
        }

        if (circuit.containsKey("a")) {
            part1Res = signal("a");

            // Part 2: override wire b with part 1's signal, reset all wires and rerun
            circuit.put("b", new String[] {String.valueOf(part1Res)});
            cache.clear();
            part2Res = signal("a");
        } else {
            // The example has no wire "a": show every wire instead
            for (String wire : circuit.keySet()) {
                System.out.println(wire + ": " + signal(wire));
            }
        }

        System.out.println("Part 1 res: " + part1Res);
        System.out.println("Part 2 res: " + part2Res);
    }
}
