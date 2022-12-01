package Day6;

import java.util.*;
import java.io.*;

public class Day6 {
    static ArrayList<Integer> fromStrToInt(String[] strArray) {
        int lengthArray = strArray.length;
        ArrayList<Integer> intArray = new ArrayList<Integer>();

        for (int i = 0; i < lengthArray; i++) {
            intArray.add(Integer.parseInt(strArray[i]));
        }
        return intArray;
    }

    static int partA(Scanner fileReader) {
        String[] strNumbers = fileReader.nextLine().split(",");
        ArrayList<Integer> intNumbers = fromStrToInt(strNumbers);

        for (int i = 0; i < 80; i++) {
            int currentSize = intNumbers.size();
            for (int j = 0; j < currentSize; j++) {
                int currentNumber = intNumbers.get(j);
                if (currentNumber > 0) {
                    intNumbers.set(j, currentNumber - 1);
                } else if (currentNumber == 0) {
                    intNumbers.set(j, 6);
                    intNumbers.add(8);
                }
            }
        }

        return intNumbers.size();
    }

    static int partB(Scanner fileReader) {
        // We need a NON QUADRATIC ALGORITHM
        return 0;
    }

    public static void main(String[] args) {
        try {
            String dataPath = "Day6/day6_data.txt";
            //String examplePath = "Day6/day6_example.txt";
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