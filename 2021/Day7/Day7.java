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
        return (number * (number + 1)) / 2;
    }

    static int minCost(int[] array) {
        int minNumber = array[0];
        for (int number : array) {
            if (number < minNumber) {
                minNumber = number;
            }
        }

        return minNumber;
    }

    static int partB(Scanner fileReader) {
        int[] numbers = strArrToInt(fileReader.nextLine().split(","));
        int[] costs = new int[numbers.length];
        
        for (int i = 0; i < numbers.length; i++) {
            int cost = 0;
            for (int j = 0; j < numbers.length; j++) {
                cost += summatory(Math.abs(i - numbers[j]));
            }
            costs[i] = cost;
        }

        return minCost(costs);
    }

    public static void main(String[] args) {
        try {
            String dataPath = "Day7/day7_data.txt";
            //String examplePath = "Day7/day7_example.txt";
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