package Day5;

import java.util.*;
import java.io.*;

public class Day5 {
    private static final int MAXSIZEDATA = 1000;
    private static final int MAXSIZEEXAMPLE = 10;

    static int[] arrayNumLine(String line) {
        // The format of the line is "num1,num2 -> num3,num4"
        // Split first by " -> "
        String[] firstSplit = line.split(" -> ");
        String[] firstPart = firstSplit[0].split(",");
        String[] secondPart = firstSplit[1].split(",");

        int[] numArray = new int[4];
        numArray[0] = Integer.parseInt(firstPart[0]);
        numArray[1] = Integer.parseInt(firstPart[1]);
        numArray[2] = Integer.parseInt(secondPart[0]);
        numArray[3] = Integer.parseInt(secondPart[1]);
        
        return numArray;
    }

    /**
     * 
     * @param fileReader the file from where we have to read the data
     * @param maxSize the maximum size of the array. That is, the maximum x or y coordinate from the data file.
     * @return the total points from horizontal or vertical lines that overlap
     */
    static int partA(Scanner fileReader, int maxSize) {
        int[][] allPointsCounter = new int[maxSize][maxSize];
        int totalDuplicates = 0;
        while (fileReader.hasNext()) {
            // We extract the points that belong to an horiontal or vertical line
            // We have to keep track of the biggest one of them all
            int[] numArray = arrayNumLine(fileReader.nextLine());
            
            int x1 = numArray[0];
            int y1 = numArray[1];
            int x2 = numArray[2];
            int y2 = numArray[3];
            
            if (x1 == x2) {
                // Adding all the points in between
                for (int i = Math.min(y1, y2); i <= Math.max(y1, y2); i++) {
                    allPointsCounter[x1][i] += 1;
                }
            } else if (y1 == y2) {
                // Adding all the points in between
                for (int i = Math.min(x1, x2); i <= Math.max(x1, x2); i++) {
                    allPointsCounter[i][y1] += 1;
                }
            }
        }

        // Counting the number of times where two or more points overlap
        for (int i = 0; i < allPointsCounter.length; i++) {
            for (int j = 0; j < allPointsCounter.length; j++) {
                if (allPointsCounter[i][j] > 1) {
                    totalDuplicates += 1;
                }
            }
        }

        return totalDuplicates;
    }

    /**
     * 
     * @param fileReader the file from where we have to read the data
     * @param maxSize the maximum size of the array. That is, the maximum x or y coordinate from the data file.
     * @return the total points from horizontal or vertical lines that overlap
     */
    static int partB(Scanner fileReader, int maxSize) {
        // We now need to consider diagonal lines as well.
        int[][] allPointsCounter = new int[maxSize][maxSize];
        int totalDuplicates = 0;
        while (fileReader.hasNext()) {
            // We extract the points that belong to an horiontal or vertical line
            // We have to keep track of the biggest one of them all
            int[] numArray = arrayNumLine(fileReader.nextLine());
            
            int x1 = numArray[0];
            int y1 = numArray[1];
            int x2 = numArray[2];
            int y2 = numArray[3];
            
            if (x1 == x2) {
                // Adding all the points in between
                for (int i = Math.min(y1, y2); i <= Math.max(y1, y2); i++) {
                    allPointsCounter[x1][i] += 1;
                }
            } else if (y1 == y2) {
                // Adding all the points in between
                for (int i = Math.min(x1, x2); i <= Math.max(x1, x2); i++) {
                    allPointsCounter[i][y1] += 1;
                }
            } else {
                // Diagonal lines case
                // We will always start with the point of minimum x. So we will always increase x by one to x2.
                // Increase or decrease y will depend on whether the destination point is above or below the origin.
                int startX = Math.min(x1, x2);
                int endX = Math.max(x1, x2);
                int startY, endY;
                if (startX == x1) {
                    startY = y1;
                    endY = y2;
                } else {
                    startY = y2;
                    endY = y1;  
                }
                for (int i = startX; i <= endX; i++) {
                    allPointsCounter[i][startY] += 1;
                    if (startY < endY) {
                        startY += 1;
                    } else {
                        startY -= 1;
                    }
                }
            }
        }

        // Counting the number of times where two or more points overlap
        for (int i = 0; i < allPointsCounter.length; i++) {
            for (int j = 0; j < allPointsCounter.length; j++) {
                if (allPointsCounter[i][j] > 1) {
                    totalDuplicates += 1;
                }
            }
        }

        return totalDuplicates;
    }

    public static void main(String[] args) {
        try {
            String dataPath = "Day5/day5_data.txt";
            //String examplePath = "Day5/day5_example.txt";
            Scanner fileReaderA = new Scanner(new File(dataPath));
            Scanner fileReaderB = new Scanner(new File(dataPath));
            
            
            // Data
            System.out.println("Final result part a: " + partA(fileReaderA, MAXSIZEDATA));
            fileReaderA.close();
            System.out.println("Final result part b: " + partB(fileReaderB, MAXSIZEDATA));
            fileReaderB.close();

        } catch (FileNotFoundException e) {
            System.out.println("The file could not be found");
            e.printStackTrace();
        }
    }
}