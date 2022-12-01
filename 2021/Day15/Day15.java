package Day15;

import java.util.*;

import java.io.*;

class Point {
    private int risk;
    private boolean visited;

    public Point(int risk) {
        this.risk = risk;
        visited = false;
    }

    public int getRisk() { return risk; }
    public boolean isVisited() { return visited; }
    public void setVisited() { visited = true; }
}

public class Day15 {

    static List<List<Integer>> fillPathList(Point[][] points, int numRows, int numColumns, int currentRow, int currentColumn, List<Integer> currentPath, List<List<Integer>> allPaths) {
        if (currentRow > numRows - 1 || currentColumn > numColumns - 1) {
            return allPaths;
        } else {
            currentPath.add(points[currentRow][currentColumn].getRisk());
            if (currentColumn == numColumns - 1 && currentRow == numRows - 1) {
                allPaths.add(new ArrayList<Integer>(currentPath));
            }
            allPaths = fillPathList(points, numRows, numColumns, currentRow, currentColumn + 1, currentPath, allPaths); // Left
            allPaths = fillPathList(points, numRows, numColumns, currentRow + 1, currentColumn, currentPath, allPaths); // Down
            currentPath.remove(currentPath.size() - 1);
            return allPaths;
        }
    }
    
    static int additionList(List<Integer> list) {
        int addition = 0;
        for (int i = 0; i < list.size(); i++) {
            addition += list.get(i);
        }

        return addition;
    }

    static int minVertex(int[] distance, boolean[] visited) {
        int minVertex = -1;
        for (int i = 0; i < distance.length; i++) {
            if (visited[i] == false && (minVertex == -1 || distance[i] < distance[minVertex])) {
                minVertex = i;
            }
        }
        return minVertex;
    }

    static void djikstra(int[][] nodes, int src) {
        int length = nodes.length;
        boolean visited[] = new boolean[length];
        int distance[] = new int[length];
        distance[src] = 0;
        for (int i = 1; i < length; i++) {
            distance[i] = Integer.MAX_VALUE;
        }

        for (int i = 0; i < length - 1; i++) {
            // Vertex with minimum distance
            int minVertex = minVertex(distance, visited);

            for (int j = 0; j < length; j++) {
                if (nodes[minVertex][j] != 0 && visited[j] == false && distance[minVertex] != Integer.MAX_VALUE) {
                    int newDistance = distance[minVertex] + nodes[minVertex][j];
                    if (newDistance < distance[j]) {
                        distance[j] = newDistance;
                    }
                }
            }
        }
        for (int i = 1; i < length; i++) {
            System.out.println(i + " " + distance[i]);
        }

    }
    
    static int partA(Scanner fileReader, int numRows, int numColumns) {
        Point[][] riskMatrix = new Point[numRows][numColumns];
        List<Integer> pathRisk = new ArrayList<Integer>();
        int currentRow = 0;
        while(fileReader.hasNext()) {
            // Filling the matrix
            String currentString = fileReader.nextLine();
            for (int j = 0; j < numColumns; j++) {
                riskMatrix[currentRow][j] = new Point(Integer.valueOf(String.valueOf(currentString.charAt(j))));
            }
            currentRow += 1;
        }
        List<List<Integer>> allPaths = new ArrayList<List<Integer>>();
        
        allPaths = fillPathList(riskMatrix, numRows, numColumns, 0, 0, pathRisk, allPaths);
        int minRisk = additionList(allPaths.remove(0));
        for (int i = 1; i < allPaths.size(); i++) {
            List<Integer> currentList = allPaths.remove(i);
            int addition = additionList(currentList);
            if (addition < minRisk) {
                minRisk = addition;
            }
        }
        return minRisk - riskMatrix[0][0].getRisk();
    }

    static int partB(Scanner fileReader) {
        return 0;
    }

    public static void main(String[] args) {
        try {
            String dataPath = "Day15/day15_data.txt";
            int numRows = 100, numColumns = 100;
            //String examplePath = "Day15/day15_example.txt";
            //int numRows = 10, numColumns = 10;
            Scanner fileReaderA = new Scanner(new File(dataPath));
            Scanner fileReaderB = new Scanner(new File(dataPath));
            
            
            // Data
            System.out.println("Final result part a: " + partA(fileReaderA, numRows, numColumns));
            fileReaderA.close();
            System.out.println("Final result part b: " + partB(fileReaderB));
            fileReaderB.close();

        } catch (FileNotFoundException e) {
            System.out.println("The file could not be found");
            e.printStackTrace();
        }
    }
}