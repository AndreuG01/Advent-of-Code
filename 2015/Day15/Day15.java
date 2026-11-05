import java.nio.file.*;
import java.util.*;

public class Day15 {
    static String readText(String path) throws Exception {
        return Files.readString(Path.of(path)).strip();
    }

    static List<String> readLines(String path) throws Exception {
        return readText(path).lines().toList();
    }

    static List<int[]> multipliers = new ArrayList<>();
    static int[] calories;
    static long part1Res = 0;
    static long part2Res = 0;

    static long dot(int[] prop, int[] amounts) {
        long total = 0;
        for (int i = 0; i < prop.length; i++) total += (long) prop[i] * amounts[i];
        return total;
    }

    static void checkCookie(int[] amounts) {
        long currRes = 1;
        for (int[] prop : multipliers) currRes *= Math.max(dot(prop, amounts), 0);
        part1Res = Math.max(part1Res, currRes);
        // Part 2: only cookies with exactly 500 calories
        if (dot(calories, amounts) == 500) part2Res = Math.max(part2Res, currRes);
    }

    static void combinationsSum(int position, int total, int[] amounts) {
        if (position == amounts.length - 1) {
            // The last value has to be whatever is left
            amounts[position] = total;
            checkCookie(amounts);
            return;
        }
        for (int first = 0; first <= total; first++) {
            amounts[position] = first;
            combinationsSum(position + 1, total - first, amounts);
        }
    }

    public static void main(String[] args) throws Exception {
        List<String> fileContent = readLines(args[0]);

        int numElems = fileContent.size();
        for (int i = 0; i < 4; i++) multipliers.add(new int[numElems]);
        calories = new int[numElems];

        for (int i = 0; i < numElems; i++) {
            String[] splitedElems = fileContent.get(i).replace(",", "").split(" ");
            multipliers.get(0)[i] = Integer.parseInt(splitedElems[2]);
            multipliers.get(1)[i] = Integer.parseInt(splitedElems[4]);
            multipliers.get(2)[i] = Integer.parseInt(splitedElems[6]);
            multipliers.get(3)[i] = Integer.parseInt(splitedElems[8]);
            calories[i] = Integer.parseInt(splitedElems[10]);
        }

        combinationsSum(0, 100, new int[numElems]);

        System.out.println("Part 1 res: " + part1Res);
        System.out.println("Part 2 res: " + part2Res);
    }
}
