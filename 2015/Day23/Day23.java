import java.nio.file.*;
import java.util.*;

public class Day23 {
    static String readText(String path) throws Exception {
        return Files.readString(Path.of(path)).strip();
    }

    static List<String> readLines(String path) throws Exception {
        return readText(path).lines().toList();
    }

    static Map<String, Long> run(List<String[]> instructions, long a, long b) {
        Map<String, Long> registers = new HashMap<>(Map.of("a", a, "b", b));
        int pc = 0;
        while (pc >= 0 && pc < instructions.size()) {
            String[] instruction = instructions.get(pc);
            String action = instruction[0];
            if (action.equals("hlf")) {
                registers.put(instruction[1], registers.get(instruction[1]) / 2);
            } else if (action.equals("tpl")) {
                registers.put(instruction[1], registers.get(instruction[1]) * 3);
            } else if (action.equals("inc")) {
                registers.put(instruction[1], registers.get(instruction[1]) + 1);
            } else if (action.equals("jmp")) {
                pc += Integer.parseInt(instruction[1]);
                continue;
            } else if (action.equals("jie") && registers.get(instruction[1]) % 2 == 0) {
                pc += Integer.parseInt(instruction[2]);
                continue;
            } else if (action.equals("jio") && registers.get(instruction[1]) == 1) {  // jump if ONE, not if odd
                pc += Integer.parseInt(instruction[2]);
                continue;
            }
            pc += 1;
        }
        return registers;
    }

    public static void main(String[] args) throws Exception {
        List<String> fileContent = readLines(args[0]);

        List<String[]> instructions = new ArrayList<>();
        for (String line : fileContent) instructions.add(line.replace(",", "").split(" "));

        Map<String, Long> registers = run(instructions, 0, 0);
        // The puzzle's example asks for register a
        long part1Res = args[0].contains("example") ? registers.get("a") : registers.get("b");

        // Part 2: same program, but register a starts at 1
        long part2Res = run(instructions, 1, 0).get("b");

        System.out.println("Part 1 res: " + part1Res);
        System.out.println("Part 2 res: " + part2Res);
    }
}
