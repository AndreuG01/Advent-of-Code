package Day13;

import java.util.*;

import java.io.*;

class Point {
    private int row;
    private int column;

    public Point(int row, int column) {
        this.row = row;
        this.column = column;
    }

    public int getRow() { return row; }
    public int getColumn() { return column; }
}

class FoldPoint {
    int value;
    String coordinate;

    public FoldPoint(int value, String coordinate) {
        this.value = value;
        this.coordinate = coordinate;
    }

    public int getValue() { return value; }
    public boolean isHorizontal() {
        return coordinate.equals("y");
    }
}

public class Day13 {
    static void setZeroFromRow(int[][] matrix, int row) {
        int numRows = matrix.length;
        int numColumns = matrix[0].length;
        for (int i = row; i < numRows; i++) {
            for (int j = 0; j < numColumns; j++) {
                matrix[i][j] = 0;
            }
        }
    }

    static int countVisible(int[][] matrix) {
        int numRow = matrix.length;
        int numColumns = matrix[0].length;
        int visible = 0;
        for (int i = 0; i < numRow; i++) {
            for (int j = 0; j < numColumns; j++) {
                if (matrix[i][j] == 1) {
                    visible += 1;
                }
            }
        }

        return visible;
    }

    static boolean rowIsZero(int[][] matrix, int row) {
        int numColumns = matrix[0].length;
        for (int column = 0; column < numColumns; column++) {
            if (matrix[row][column] == 1) {
                return false;
            }
        }
        return true;
    }
    
    static boolean columnIsZero(int[][] matrix, int column) {
        int numRows = matrix.length;
        for (int row = 0; row < numRows; row++) {
            if (matrix[row][column] == 1) {
                return false;
            }
        }
        return true;
    }

    static void printMatrix(int[][] matrix) {
        int biggestRow = matrix.length;
        int biggestColumn = matrix[0].length;
        for (int i = 0; i < biggestRow; i++) {
            if (rowIsZero(matrix, i) == false) { // If the whole row is 0, we do not want to print it. It means that we have folded that part of the paper.
                for (int j = 0; j < biggestColumn; j++) {
                    if (columnIsZero(matrix, j) == false) { // Same reasoning as for the rows.
                        if (matrix[i][j] == 1) {
                            System.out.print("*");
                        } else {
                            System.out.print(" ");
                        }
                    }
                }
            System.out.println("");
            }
        }
    }

    static void setZeroFromColumn(int[][] matrix, int column) {
        int numRows = matrix.length;
        int numColumns = matrix[0].length;
        for (int i = 0; i < numRows; i++) {
            for (int j = column; j < numColumns; j++) {
                matrix[i][j] = 0;
            }
        }
    }
    static int partA(Scanner fileReader) {
        int biggestRow = 0;
        int biggestColumn = 0;
        boolean fold = false;
        List<FoldPoint> foldPoints = new ArrayList<FoldPoint>();
        List<Point> allPoints = new ArrayList<Point>();
        while (fileReader.hasNext()) {
            String currentLine = fileReader.nextLine();
            // A white line separates the coordinates and the fold instructions
            if (currentLine.equals("")) {
                fold = true;
            }
            if (fold == false) {
                String[] coordinates = currentLine.split(",");
                int column = Integer.parseInt(coordinates[0]);
                int row = Integer.parseInt(coordinates[1]);
                allPoints.add(new Point(row, column)); // Saving all the points
                if (column > biggestColumn) {
                    biggestColumn = column;
                }
                if (row > biggestRow) {
                    biggestRow = row;
                }
                
            } else {
                if (currentLine.contains("x")) {
                    foldPoints.add(new FoldPoint(Integer.parseInt(currentLine.replaceAll("[^0-9]", "")), "x"));
                } else if (currentLine.contains("y")) {
                    foldPoints.add(new FoldPoint(Integer.parseInt(currentLine.replaceAll("[^0-9]", "")), "y"));
                }
            }
            
        }
        
        // Initializing the matrix
        int[][] matrix = new int[biggestRow + 1][biggestColumn + 1];
        for (int i = 0; i < allPoints.size(); i++) {
            Point currentPoint = allPoints.get(i);
            matrix[currentPoint.getRow()][currentPoint.getColumn()] = 1;
        }
        
        for (int i = 0; i < 1; i++) { // For part a, we just need to do 1 fold
            FoldPoint currentFoldPoint = foldPoints.get(i);
            if (currentFoldPoint.isHorizontal()) {
                // Horizontal fold
                int foldCoordinate = currentFoldPoint.getValue();
                int correspondingRow = foldCoordinate - 1;
                for (int row = foldCoordinate + 1; row < biggestRow + 1; row++) {
                    for (int column = 0; column < biggestColumn + 1; column++) {
                        if (matrix[row][column] == 1) {
                            matrix[correspondingRow][column] = 1;
                        }
                    }
                    correspondingRow -= 1;
                }
                setZeroFromRow(matrix, foldCoordinate);
            } else {
                // Vertical fold
                int foldCoordinate = currentFoldPoint.getValue();
                int correspondingColumn = foldCoordinate - 1;
                for (int row = 0; row < biggestRow + 1; row++) {
                    correspondingColumn = foldCoordinate - 1;
                    for (int column = foldCoordinate + 1; column < biggestColumn + 1; column++) {
                        if (matrix[row][column] == 1) {
                            matrix[row][correspondingColumn] = 1;
                        }
                        correspondingColumn -= 1;
                    }
                }
                setZeroFromColumn(matrix, foldCoordinate);
            }
        }

        return countVisible(matrix);
    }

    static void partB(Scanner fileReader) {
        int biggestRow = 0;
        int biggestColumn = 0;
        boolean fold = false;
        List<FoldPoint> foldPoints = new ArrayList<FoldPoint>();
        List<Point> allPoints = new ArrayList<Point>();
        while (fileReader.hasNext()) {
            String currentLine = fileReader.nextLine();
            // A white line separates the coordinates and the fold instructions
            if (currentLine.equals("")) {
                fold = true;
            }
            if (fold == false) {
                String[] coordinates = currentLine.split(",");
                int column = Integer.parseInt(coordinates[0]);
                int row = Integer.parseInt(coordinates[1]);
                allPoints.add(new Point(row, column)); // Saving all the points
                if (column > biggestColumn) {
                    biggestColumn = column;
                }
                if (row > biggestRow) {
                    biggestRow = row;
                }
                
            } else {
                if (currentLine.contains("x")) {
                    foldPoints.add(new FoldPoint(Integer.parseInt(currentLine.replaceAll("[^0-9]", "")), "x"));
                } else if (currentLine.contains("y")) {
                    foldPoints.add(new FoldPoint(Integer.parseInt(currentLine.replaceAll("[^0-9]", "")), "y"));
                }
            }
        }
        
        // Initializing the matrix
        int[][] matrix = new int[biggestRow + 1][biggestColumn + 1];
        for (int i = 0; i < allPoints.size(); i++) {
            Point currentPoint = allPoints.get(i);
            matrix[currentPoint.getRow()][currentPoint.getColumn()] = 1;
        }
        
        int totalFold = foldPoints.size();
        for (int i = 0; i < totalFold; i++) { // For part a, we just need to do 1 fold
            FoldPoint currentFoldPoint = foldPoints.get(i);
            if (currentFoldPoint.isHorizontal()) {
                // Horizontal fold
                int foldCoordinate = currentFoldPoint.getValue();
                int correspondingRow = foldCoordinate - 1;
                for (int row = foldCoordinate + 1; row < biggestRow + 1; row++) {
                    for (int column = 0; column < biggestColumn + 1; column++) {
                        if (matrix[row][column] == 1) {
                            matrix[correspondingRow][column] = 1;
                        }
                    }
                    correspondingRow -= 1;
                }
                setZeroFromRow(matrix, foldCoordinate);
            } else {
                // Vertical fold
                int foldCoordinate = currentFoldPoint.getValue();
                int correspondingColumn = foldCoordinate - 1;
                for (int row = 0; row < biggestRow + 1; row++) {
                    correspondingColumn = foldCoordinate - 1;
                    for (int column = foldCoordinate + 1; column < biggestColumn + 1; column++) {
                        if (matrix[row][column] == 1) {
                            matrix[row][correspondingColumn] = 1;
                        }
                        correspondingColumn -= 1;
                    }
                }
                setZeroFromColumn(matrix, foldCoordinate);
            }
        }
        printMatrix(matrix);
    }

    public static void main(String[] args) {
        try {
            String dataPath = "Day13/day13_data.txt";
            //String examplePath = "Day13/day13_example.txt";
            Scanner fileReaderA = new Scanner(new File(dataPath));
            Scanner fileReaderB = new Scanner(new File(dataPath));
            
            
            // Data
            System.out.println("Final result part a: " + partA(fileReaderA));
            fileReaderA.close();
            partB(fileReaderB);
            fileReaderB.close();

        } catch (FileNotFoundException e) {
            System.out.println("The file could not be found");
            e.printStackTrace();
        }
    }
}