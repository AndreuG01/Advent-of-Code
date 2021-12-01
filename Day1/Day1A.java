package Day1;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Day1A {
    static int partA(Scanner fileReader) {
        int numIncreases = 0;
        int previousNumber = fileReader.nextInt();
        while (fileReader.hasNext()) {
            int currentNumber = fileReader.nextInt();
            if (currentNumber > previousNumber) {
                numIncreases += 1;
            }
            previousNumber = currentNumber;
        }
        return numIncreases;
    }

    static int partB(Scanner fileReader) {
        ArrayList<Integer> storedData = new ArrayList<Integer>();
        int idx = 0;
        int numIncreases = 0;
        while (fileReader.hasNext()) {
            storedData.add(fileReader.nextInt());
            if (idx >= 3) {
                int currentSum = storedData.get(idx) + storedData.get(idx - 1) + storedData.get(idx - 2);
                int previousSum = storedData.get(idx - 1) + storedData.get(idx - 2) + storedData.get(idx - 3);
                if (currentSum > previousSum) {
                    numIncreases += 1;
                }
            }
            idx += 1;
        }

        return numIncreases;
    }
    public static void main(String[] args) {
        try {
            String dataPath = "Day1/day1_data.txt";
            String examplePath = "Day1/day1_example.txt";
            File inputData = new File(dataPath);
            //File inputData = new File(examplePath);
            Scanner fileReaderA = new Scanner(inputData);
            Scanner fileReaderB = new Scanner(inputData);
            

            System.out.println("Number of increases part a: " + partA(fileReaderA));
            fileReaderA.close();
            System.out.println("Number of increases part b: " + partB(fileReaderB));
            fileReaderB.close();

        } catch (FileNotFoundException e) {
            System.out.println("The file could not be found");
            e.printStackTrace();
        }
    }
}