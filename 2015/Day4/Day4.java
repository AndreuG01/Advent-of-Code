import java.nio.file.*;
import java.security.MessageDigest;
import java.util.*;

public class Day4 {
    static String readText(String path) throws Exception {
        return Files.readString(Path.of(path)).strip();
    }

    static List<String> readLines(String path) throws Exception {
        return readText(path).lines().toList();
    }

    public static void main(String[] args) throws Exception {
        String fileContent = readText(args[0]);

        int part1Res = 0;
        int part2Res = 0;
        boolean part1Done = false;

        MessageDigest md5 = MessageDigest.getInstance("MD5");
        int count = 1;
        while (true) {
            byte[] res = md5.digest((fileContent + count).getBytes());
            // Each byte is two hex digits
            boolean fiveZeros = res[0] == 0 && res[1] == 0 && (res[2] & 0xff) < 16;
            boolean sixZeros = res[0] == 0 && res[1] == 0 && res[2] == 0;
            if (fiveZeros && !part1Done) {
                part1Res = count;
                part1Done = true;
            }
            if (sixZeros) {
                part2Res = count;
                break;
            }
            count += 1;
        }

        System.out.println("Part 1 res: " + part1Res);
        System.out.println("Part 2 res: " + part2Res);
    }
}
