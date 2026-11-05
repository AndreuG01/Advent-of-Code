import java.nio.file.*;
import java.util.*;

public class Day12 {
    static String readText(String path) throws Exception {
        return Files.readString(Path.of(path)).strip();
    }

    static List<String> readLines(String path) throws Exception {
        return readText(path).lines().toList();
    }

    // Java has no JSON in its standard library, so here is a small parser for what the input uses
    static class Value {
        Long number = null;
        String text = null;
        boolean isObject = false;
        List<Value> children = new ArrayList<>();  // array elements or object values
    }

    static String json;
    static int i = 0;

    static String parseString() {
        int end = json.indexOf('"', i + 1);
        String text = json.substring(i + 1, end);
        i = end + 1;
        return text;
    }

    static Value parseValue() {
        Value value = new Value();
        char c = json.charAt(i);
        if (c == '[' || c == '{') {
            value.isObject = c == '{';
            char closing = value.isObject ? '}' : ']';
            i += 1;
            while (json.charAt(i) != closing) {
                if (json.charAt(i) == ',') i += 1;
                if (value.isObject) {
                    parseString();  // the key
                    i += 1;         // the colon
                }
                value.children.add(parseValue());
            }
            i += 1;
        } else if (c == '"') {
            value.text = parseString();
        } else {
            int start = i;
            while (json.charAt(i) == '-' || Character.isDigit(json.charAt(i))) i += 1;
            value.number = Long.parseLong(json.substring(start, i));
        }
        return value;
    }

    static long sumNumbers(Value obj, boolean ignoreRed) {
        // Walk the JSON recursively and add up every number found
        if (obj.number != null) return obj.number;
        if (obj.text != null) return 0;
        if (obj.isObject && ignoreRed) {
            // Part 2: skip any object (not array) that has "red" as a value
            for (Value child : obj.children) {
                if ("red".equals(child.text)) return 0;
            }
        }
        long total = 0;
        for (Value child : obj.children) total += sumNumbers(child, ignoreRed);
        return total;
    }

    public static void main(String[] args) throws Exception {
        json = readText(args[0]);

        Value jsonObj = parseValue();

        long part1Res = sumNumbers(jsonObj, false);
        long part2Res = sumNumbers(jsonObj, true);

        System.out.println("Part 1 res: " + part1Res);
        System.out.println("Part 2 res: " + part2Res);
    }
}
