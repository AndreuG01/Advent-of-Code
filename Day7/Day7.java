package Day7;

import java.util.*;
import java.io.*;

public class Day7 {
    static int[] strArrToInt(String[] stringArray) {
        int[] intArray = new int[stringArray.length];
        for (int i = 0; i < stringArray.length; i++) {
            intArray[i] = Integer.parseInt(stringArray[i]);
        }

        return intArray;
    }

    static int partA(Scanner fileReader) {
        int[] numbers = strArrToInt(fileReader.nextLine().split(","));
        // If we sort the array, the position that will be closer to all the others will be the mid position
        Arrays.sort(numbers);
        int fuel = 0;
        int midPosition = numbers[numbers.length / 2];
        for (int i = 0; i < numbers.length; i++) {
            fuel += Math.abs(numbers[i] - midPosition);
        }
        return fuel;
    }

    static int summatory(int number) {
        int result = number;
        for (int i = 0; i < number; i++) {
            result += i;
        }

        return result;
    }

    static int partB(Scanner fileReader) {
        return 0;
    }

    public static void main(String[] args) {
        try {
            String dataPath = "Day7/day7_data.txt";
            String examplePath = "Day7/day7_example.txt";
            Scanner fileReaderA = new Scanner(new File(examplePath));
            Scanner fileReaderB = new Scanner(new File(examplePath));
            
            
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