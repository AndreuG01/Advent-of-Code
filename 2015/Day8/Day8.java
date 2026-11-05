import java.nio.file.*;
import java.util.*;

public class Day8 {
    static String readText(String path) throws Exception {
        return Files.readString(Path.of(path)).strip();
    }

    static List<String> readLines(String path) throws Exception {
        return readText(path).lines().toList();
    }

    static int memoryLength(String line) {
        String inner = line.substring(1, line.length() - 1);  // drop the surrounding quotes
        int i = 0;
        int memLen = 0;
        while (i < inner.length()) {
            if (inner.charAt(i) == '\\') i += inner.charAt(i + 1) == 'x' ? 4 : 2;
            else i += 1;
            memLen += 1;
        }
        return memLen;
    }

    public static void main(String[] args) throws Exception {
        List<String> fileContent = readLines(args[0]);

        int part1Res = 0;
        int part2Res = 0;

        for (String line : fileContent) {
            part1Res += line.length() - memoryLength(line);
            // Encoding adds the 2 new quotes and one backslash for each " and backslash
            part2Res += 2 + line.chars().filter(c -> c == '"' || c == '\\').count();
        }

        System.out.println("Part 1 res: " + part1Res);
        System.out.println("Part 2 res: " + part2Res);
    }
}
