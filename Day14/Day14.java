package Day14;

import java.util.*;

import java.io.*;

public class Day14 {

    static int findMax(Collection<Integer> list) {
        Iterator<Integer> iterator = list.iterator();
        int max = 0;
        while (iterator.hasNext()) {
            int currentElement = iterator.next();
            if (currentElement > max) {
                max = currentElement;
            }
        }
        return max;
    }

    static int findMin(Collection<Integer> list) {
        Iterator<Integer> iterator = list.iterator();
        int min = iterator.next();
        while (iterator.hasNext()) {
            int currentElement = iterator.next();
            if (currentElement < min) {
                min = currentElement;
            }
        }
        return min;
    }
    
    static int partA(Scanner fileReader) {
        Map<String, String> intersectionRules = new HashMap<String, String>();
        String polymerTemplate = fileReader.nextLine();
        String newPolymer = "";
        fileReader.nextLine();
        while (fileReader.hasNext()) {
            String currentLine = fileReader.nextLine();
            String[] currentRule = currentLine.split(" -> ");
            intersectionRules.put(currentRule[0], currentRule[1]);
        }

        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < polymerTemplate.length() - 1; j++) {
                String currentPair = polymerTemplate.substring(j, j + 2);
                if (intersectionRules.containsKey(currentPair)) {
                    if (j == 0) {
                        newPolymer += currentPair.charAt(0);
                    }
                    newPolymer += intersectionRules.get(currentPair);
                    newPolymer += currentPair.charAt(1);
                } else {
                    newPolymer += currentPair;
                }
            }
            polymerTemplate = newPolymer;
            newPolymer = "";
        }

        // Now we need to count the occurrences of all the letters
        Map<String, Integer> letterOccurrences = new HashMap<String, Integer>();
        Set<String> letters = new HashSet<String>();
        int polymerLength = polymerTemplate.length();
        for (int i = 0; i < polymerLength; i++) {
            String currentLetter = String.valueOf(polymerTemplate.charAt(i));
            if (letters.contains(currentLetter)) {
                letterOccurrences.put(currentLetter, letterOccurrences.get(currentLetter) + 1);
            } else {
                letters.add(currentLetter);
                letterOccurrences.put(currentLetter, 1);
            }
        }

        Collection<Integer> occurrences = letterOccurrences.values();
        int max = findMax(occurrences);
        int min = findMin(occurrences);
        return max - min;
    }

    static int partB(Scanner fileReader) {
        return 0;
    }

    public static void main(String[] args) {
        try {
            String dataPath = "Day14/day14_data.txt";
            //String examplePath = "Day14/day14_example.txt";
            Scanner fileReaderA = new Scanner(new File(dataPath));
            Scanner fileReaderB = new Scanner(new File(dataPath));
            
            
            // Data
            System.out.println("Final result part a: " + partA(fileReaderA));
            fileReaderA.close();
            System.out.println("Final result part b: " + partB(fileReaderB));
            fileReaderB.close();

        } catch (FileNotFoundException e) {
            System.out.println("The file could not be found");
            e.printStackTrace();
        }
    }
}