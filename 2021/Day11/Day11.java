package Day11;

import java.util.*;

import java.io.*;

class Point {
    private int value;
    private boolean flashed;

    public Point(int value) {
        this.value = value;
        flashed = false;
    }

    public int getValue() { return value; }
    public void setFlashed() { flashed = true; }
    public boolean isFlashed() { return flashed; }
    public void increaseValue() { value += 1; }
    public void resetValue() { value = 0; }
    public void resetFlash() { flashed = false; }
}

public class Day11 {
    public static final int SIZE_MATRIX = 10;

    static void setVisitedFalse(Point[][] allPoints) {
        for (int i = 0; i < SIZE_MATRIX; i++) {
            for (int j = 0; j < SIZE_MATRIX; j++) {
                allPoints[i][j].resetFlash();
            }
        }
    }

    static int flash(Point[][] allPoints, int row, int column, int flashes) {
        if ((row >= 0 && row <= SIZE_MATRIX - 1) && (column >= 0 && column <= SIZE_MATRIX - 1)) {
            Point currentPoint = allPoints[row][column];
            allPoints[row][column].increaseValue();
            if (currentPoint.isFlashed() == true) {
                allPoints[row][column].resetValue();
                return flashes;
            } else {
                if (currentPoint.getValue() > 9) {
                    allPoints[row][column].setFlashed();
                    flashes += 1;
                    flashes = flash(allPoints, row + 1, column, flashes); // Down
                    flashes = flash(allPoints, row - 1, column, flashes); // Top
                    flashes = flash(allPoints, row, column - 1, flashes); // Left
                    flashes = flash(allPoints, row, column + 1, flashes); // Right
                    flashes = flash(allPoints, row + 1, column + 1, flashes); // Diagonal down right
                    flashes = flash(allPoints, row + 1, column - 1, flashes); // Diagonal down left
                    flashes = flash(allPoints, row - 1, column + 1, flashes); // Diagonal top right
                    flashes = flash(allPoints, row - 1, column - 1, flashes); // Diagonal top left
                    allPoints[row][column].resetValue();
                    return flashes;
                } else {
                    
                }
                return flashes;
            }
        }
        return flashes;
    }
    
    static int partA(Scanner fileReader) {
        Point[][] points = new Point[SIZE_MATRIX][SIZE_MATRIX];
        int rowCounter = 0;
        // Adding all the points to the matrix
        while (fileReader.hasNext()) {
            String currentLine = fileReader.nextLine();
            for (int j = 0; j < SIZE_MATRIX; j++) {
                points[rowCounter][j] = new Point(Integer.parseInt(String.valueOf(currentLine.charAt(j))));
            }
            rowCounter += 1;
        }

        // Once we have all the points stored, start measuring the energy level and flashes for 100 steps
        int numFlashes = 0;
        for (int i = 0; i < 100; i++) {
            // First, we increase the energy value by 1
            for (int row = 0; row < SIZE_MATRIX; row++) {
                for (int column = 0; column < SIZE_MATRIX; column++) {
                    points[row][column].increaseValue();
                }
            }
            // We look for flashed octopus
            for (int row = 0; row < SIZE_MATRIX; row++) {
                for (int column = 0; column < SIZE_MATRIX; column++) {
                    if (points[row][column].getValue() > 9) {
                        numFlashes += flash(points, row, column, 0);
                    }
                }
            }
            
            // At the end of every step, we have to reset all the visited state to false
            setVisitedFalse(points);
        }

        return numFlashes;
    }

    static boolean flashedSimultaneously(Point[][] allPoints) {
        for (int i = 0; i < SIZE_MATRIX; i++) {
            for (int j = 0; j < SIZE_MATRIX; j++) {
                if (allPoints[i][j].getValue() != 0) {
                    return false;
                }
            }
        }

        return true;
    }

    static int partB(Scanner fileReader) {
        Point[][] points = new Point[SIZE_MATRIX][SIZE_MATRIX];
        int rowCounter = 0;
        // Adding all the points to the matrix
        while (fileReader.hasNext()) {
            String currentLine = fileReader.nextLine();
            for (int j = 0; j < SIZE_MATRIX; j++) {
                points[rowCounter][j] = new Point(Integer.parseInt(String.valueOf(currentLine.charAt(j))));
            }
            rowCounter += 1;
        }

        // Once we have all the points stored, start measuring the energy level and flashes for 100 steps
        int stepNumber = 0;
        while (flashedSimultaneously(points) == false) {
            // First, we increase the energy value by 1
            for (int row = 0; row < SIZE_MATRIX; row++) {
                for (int column = 0; column < SIZE_MATRIX; column++) {
                    points[row][column].increaseValue();
                }
            }
            // We look for flashed octopus
            for (int row = 0; row < SIZE_MATRIX; row++) {
                for (int column = 0; column < SIZE_MATRIX; column++) {
                    if (points[row][column].getValue() > 9) {
                        flash(points, row, column, 0);
                    }
                }
            }
            // At the end of every step, we have to reset all the visited state to false
            setVisitedFalse(points);
            stepNumber += 1;
        }

        return stepNumber;
    }

    public static void main(String[] args) {
        try {
            String dataPath = "Day11/day11_data.txt";
            //String examplePath = "Day11/day11_example.txt";
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