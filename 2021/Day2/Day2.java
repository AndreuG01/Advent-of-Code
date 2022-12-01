package Day2;

import java.util.*;
import java.io.*;

public class Day2 {
    private static final String FORWARD = "forward";
    private static final String DOWN = "down";
    private static final String UP = "up";

    static int partA(Scanner fileReader) {
        int horizontalCount = 0;
        int verticalCount = 0;

        while (fileReader.hasNext()) {
            String currentDirection = fileReader.next();
            switch (currentDirection) {
                case FORWARD:
                    horizontalCount += fileReader.nextInt(); 
                    break;
                case DOWN:
                    verticalCount += fileReader.nextInt();
                    break;
                case UP:
                    verticalCount -= fileReader.nextInt();
                    break;
                default:
                    break;
            }
        }
        return horizontalCount * verticalCount;
    }

    static int partB(Scanner fileReader) {
        int horizontalCount = 0;
        int verticalCount = 0;
        int aim = 0;

        while (fileReader.hasNext()) {
            String currentDirection = fileReader.next();
            switch (currentDirection) {
                case FORWARD:
                    int currentNumber = fileReader.nextInt();
                    horizontalCount += currentNumber;
                    verticalCount += currentNumber * aim; 
                    break;
                case DOWN:
                    aim += fileReader.nextInt();
                    break;
                case UP:
                    aim -= fileReader.nextInt();
                    break;
                default:
                    break;
            }
        }
        return horizontalCount * verticalCount;
    }
    public static void main(String[] args) {
        try {
            String dataPath = "Day2/day2_data.txt";
            //String examplePath = "Day2/day2_example.txt";
            File inputData = new File(dataPath);
            //File inputData = new File(examplePath);
            Scanner fileReaderA = new Scanner(inputData);
            Scanner fileReaderB = new Scanner(inputData);
            

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