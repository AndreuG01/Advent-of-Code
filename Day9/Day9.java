package Day9;

import java.util.*;

import java.io.*;

class Point {
    private int value;
    private boolean visited;

    public Point(int value) {
        this.value = value;
        visited = false;
    }

    public int getValue() { return value; }
    public void setValue(int value) { this.value = value; }
    public boolean isVisited() { return visited; }
    public void setVisited() { visited = true; }
}

public class Day9 {
    
    static int partA(Scanner fileReader) {
        List<Integer> lowPoints = new ArrayList<Integer>(); // List where all the low points will be stored
        List<List<Integer>> allPoints = new ArrayList<List<Integer>>();
        while (fileReader.hasNext()) {
            // Filling the array with all the points
            String currentLine = fileReader.nextLine();
            List<Integer> currentRow = new ArrayList<Integer>();
            for (int column = 0; column < currentLine.length(); column++) {
                currentRow.add(Character.getNumericValue(currentLine.charAt(column)));
            }
            allPoints.add(currentRow);
        }

        // Determining which points are low points
        int numRows = allPoints.size();
        int numColumns = allPoints.get(0).size();
        for (int row = 0; row < numRows; row++) {
            for (int column = 0; column < numColumns; column++) {
                // The maximum value is 9, so if we initialize the values to 10, the number that we read will be always smaller.
                int top = 10;
                int down = 10;
                int left = 10;
                int right = 10;
                int currentPoint = allPoints.get(row).get(column);
                if (column != 0 && column != numColumns - 1) {
                    left = allPoints.get(row).get(column - 1);
                    right = allPoints.get(row).get(column + 1);
                } else if (column == 0) {
                    right = allPoints.get(row).get(column + 1);
                } else if (column == numColumns - 1) {
                    left = allPoints.get(row).get(column - 1);
                }

                if (row != 0 && row != numRows - 1) {
                    top = allPoints.get(row - 1).get(column);
                    down = allPoints.get(row + 1).get(column);
                } else if (row == 0) {
                    down = allPoints.get(row + 1).get(column);
                } else if (row == numRows - 1) {
                    top = allPoints.get(row - 1).get(column);
                }

                if (currentPoint < top && currentPoint < down && currentPoint < left && currentPoint < right) {
                    lowPoints.add(currentPoint);
                }
            }
        }

        int total = 0;
        for (int i = 0; i < lowPoints.size(); i++) {
            total += lowPoints.get(i) + 1;
        }

        return total;
    }

    static int sizeBassin(List<List<Point>> allPoints, int row, int column, int total, int maxRows, int maxColumns) {
        if ((row >= 0 && row <= maxRows - 1) && (column >= 0 && column <= maxColumns - 1)) {
            // The point can be accessed
            Point currentPoint = allPoints.get(row).get(column);
            if (currentPoint.getValue() == 9) {
                return total;
            } else if (currentPoint.isVisited() == false) {
                allPoints.get(row).get(column).setVisited();
                total += 1;
                total = sizeBassin(allPoints, row, column - 1, total, maxRows, maxColumns);
                total = sizeBassin(allPoints, row, column + 1, total, maxRows, maxColumns);
                total = sizeBassin(allPoints, row - 1, column, total, maxRows, maxColumns);
                total = sizeBassin(allPoints, row + 1, column, total, maxRows, maxColumns);
                return total;
            } else {
                return total;
            }
        } else {
            return total;
        }
        
    }

    static int partB(Scanner fileReader) {
        List<List<Point>> allPoints = new ArrayList<List<Point>>();
        List<Integer> bassinSizes = new ArrayList<Integer>();
        while (fileReader.hasNext()) {
            // Filling the array with all the points
            String currentLine = fileReader.nextLine();
            List<Point> currentRow = new ArrayList<Point>();
            for (int column = 0; column < currentLine.length(); column++) {
                currentRow.add(new Point(Character.getNumericValue(currentLine.charAt(column))));
            }
            allPoints.add(currentRow);
        }

        // Determining which points are low points
        int numRows = allPoints.size();
        int numColumns = allPoints.get(0).size();

        for (int row = 0; row < numRows; row++) {
            for (int column = 0; column < numColumns; column++) {
                // The maximum value is 9, so if we initialize the values to 10, the number that we read will be always smaller.
                int top = 10;
                int down = 10;
                int left = 10;
                int right = 10;
                int currentPoint = allPoints.get(row).get(column).getValue();
                if (column != 0 && column != numColumns - 1) {
                    left = allPoints.get(row).get(column - 1).getValue();
                    right = allPoints.get(row).get(column + 1).getValue();
                } else if (column == 0) {
                    right = allPoints.get(row).get(column + 1).getValue();
                } else if (column == numColumns - 1) {
                    left = allPoints.get(row).get(column - 1).getValue();
                }

                if (row != 0 && row != numRows - 1) {
                    top = allPoints.get(row - 1).get(column).getValue();
                    down = allPoints.get(row + 1).get(column).getValue();
                } else if (row == 0) {
                    down = allPoints.get(row + 1).get(column).getValue();
                } else if (row == numRows - 1) {
                    top = allPoints.get(row - 1).get(column).getValue();
                }

                if (currentPoint < top && currentPoint < down && currentPoint < left && currentPoint < right) {
                    // We store the sizes of all the bassines
                    bassinSizes.add(sizeBassin(allPoints, row, column, 0, numRows, numColumns));
                }
            }
        }
        // Now we have to find the three largest elements in the array of the sizes
        int first = 0, second = 0, third = 0;
        for (int i = 0; i < bassinSizes.size(); i++) {
            int currentSize = bassinSizes.get(i);
            if (currentSize > first) {
                third = second;
                second = first;
                first = currentSize;
            } else if (currentSize > second) {
                third = second;
                second = currentSize;
            } else if (currentSize > third) {
                third = currentSize;
            }
        }

        return first * second * third;
    }

    public static void main(String[] args) {
        try {
            String dataPath = "Day9/day9_data.txt";
            //String examplePath = "Day9/day9_example.txt";
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