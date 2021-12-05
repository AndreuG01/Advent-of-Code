package Day5;

import java.util.*;
import java.io.*;

class Point {
    private int xCoordinate;
    private int yCoordinate;

    public Point(int x, int y) {
        xCoordinate = x;
        yCoordinate = y;
    }

    public int getXCooridnate() { return xCoordinate; }
    public int getYCoordinate() { return yCoordinate; }
}

public class Day5 {

    static boolean pointIsInList(List<Point> list, Point point) {
        for (int i = 0; i < list.size(); i++) {
            Point currentPoint = list.get(i);
            if (currentPoint.getXCooridnate() == point.getXCooridnate() && currentPoint.getYCoordinate() == point.getYCoordinate()) {
                return true;
            }
        }
        return false;
    }

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

    static int partA(Scanner fileReader) {
        List<Point> allPoints = new ArrayList<Point>();
        List<Point> duplicatePoints = new ArrayList<Point>();
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
                    Point currentPoint = new Point(x1, i);
                    if (pointIsInList(allPoints, currentPoint)) {
                        if (pointIsInList(duplicatePoints, currentPoint) == false) {
                            duplicatePoints.add(currentPoint);
                            totalDuplicates += 1;
                        }
                    } else {
                        allPoints.add(new Point(x1, i));
                    }
                }
            } else if (y1 == y2) {
                // Adding all the points in between
                for (int i = Math.min(x1, x2); i <= Math.max(x1, x2); i++) {
                    Point currentPoint = new Point(i, y1);
                    if (pointIsInList(allPoints, currentPoint)) {
                        if (pointIsInList(duplicatePoints, currentPoint) == false) {
                            duplicatePoints.add(currentPoint);
                            totalDuplicates += 1;
                        }
                    } else {
                        allPoints.add(currentPoint);
                    }
                }
            }
        }
        return totalDuplicates;
    }

    static int partB(Scanner fileReader) {
        // We now need to consider diagonal lines as well.
        List<Point> allPoints = new ArrayList<Point>();
        List<Point> duplicatePoints = new ArrayList<Point>();
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
                    Point currentPoint = new Point(x1, i);
                    if (pointIsInList(allPoints, currentPoint)) {
                        if (pointIsInList(duplicatePoints, currentPoint) == false) {
                            duplicatePoints.add(currentPoint);
                            totalDuplicates += 1;
                        }
                    } else {
                        allPoints.add(new Point(x1, i));
                    }
                }
            } else if (y1 == y2) {
                // Adding all the points in between
                for (int i = Math.min(x1, x2); i <= Math.max(x1, x2); i++) {
                    Point currentPoint = new Point(i, y1);
                    if (pointIsInList(allPoints, currentPoint)) {
                        if (pointIsInList(duplicatePoints, currentPoint) == false) {
                            duplicatePoints.add(currentPoint);
                            totalDuplicates += 1;
                        }
                    } else {
                        allPoints.add(currentPoint);
                    }
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
                    Point currentPoint = new Point(i, startY);
                    if (pointIsInList(allPoints, currentPoint)) {
                        if (pointIsInList(duplicatePoints, currentPoint) == false) {
                            duplicatePoints.add(currentPoint);
                            totalDuplicates += 1;
                        }
                    } else {
                        allPoints.add(currentPoint);
                    }
                    if (startY < endY) {
                        startY += 1;
                    } else {
                        startY -= 1;
                    }
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