package Day4;

import java.util.*;


import java.io.*;

class ElementBingo {
    private int value;
    private boolean visit;

    public ElementBingo(int value) {
        this.value = value;
        visit = false;
    }

    public int getNum() { return value; }
    public boolean getState() { return visit; }
    public void markVisited() { visit = true; }
}

public class Day4 {

    static boolean bingoWins(ElementBingo[][] bingo) {
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (bingo[i][j].getState() == true) {
                    boolean win_column = bingo[0][j].getState() && bingo[1][j].getState() && bingo[2][j].getState() && bingo[3][j].getState() && bingo[4][j].getState(); 
                    boolean win_row = bingo[i][0].getState() && bingo[i][1].getState() && bingo[i][2].getState() && bingo[i][3].getState() && bingo[i][4].getState(); 
                    if (win_column || win_row) return true;
                }
            }
        }

        return false;
    }

    static ElementBingo[][] getWinningBingo(ArrayList<ElementBingo[][]> bingos) {
        for (int i = 0; i < bingos.size(); i++) {
            ElementBingo[][] currentBingo = bingos.get(i);
            if (bingoWins(currentBingo) == true) {
                return currentBingo;
            }
        }
        return null;
    }

    static void markNumberVisited(ArrayList<ElementBingo[][]> bingos, int number) {
        for (int i = 0; i < bingos.size(); i++) {
            ElementBingo[][] currentBingo = bingos.get(i);
            for (int j = 0; j < 5; j++) {
                for (int k = 0; k < 5; k++) {
                    if (currentBingo[j][k].getNum() == number) {
                        currentBingo[j][k].markVisited();
                    }
                }
            }
        }
    }

    static int getScoreBingo(ElementBingo[][] bingo, int lastNumCalled) {
        int unMarked = 0;
        for (int i = 0; i < bingo.length; i++) {
            for (int j = 0; j < bingo.length; j++) {
                if (bingo[i][j].getState() == false) {
                    unMarked += bingo[i][j].getNum();
                }
            }
        }

        return unMarked * lastNumCalled;
    }
    
    static int partA(Scanner fileReader) {
        // Reading the first numbers
        String firstLine = fileReader.nextLine();
        String[] strNumbers = firstLine.split(",");
        int[] intNumbers = new int[strNumbers.length];
        for (int i = 0; i < strNumbers.length; i++) {
            intNumbers[i] = Integer.parseInt(strNumbers[i]);
        }

        ArrayList<ElementBingo[][]> allBingos = new ArrayList<ElementBingo[][]>();

        // Filling each matrix
        int idx = 0;
        while (fileReader.hasNext())  {
            ElementBingo[][] currentBingo = new ElementBingo[5][5];
            for (int i = 0; i < 5; i++) {
                for (int j = 0; j < 5; j++) {
                    currentBingo[i][j] = new ElementBingo(fileReader.nextInt());
                }
            }
            allBingos.add(idx, currentBingo);
            idx += 1;
        }

        // Starting to play bingo
        int lastNumCalled = intNumbers[0];
        ElementBingo[][] winningBingo = null;
        for (int i = 0; i < intNumbers.length; i++) {
            lastNumCalled = intNumbers[i];
            markNumberVisited(allBingos, lastNumCalled);
            winningBingo = getWinningBingo(allBingos);
            if (winningBingo != null) {
                break;
            }
        }

        return getScoreBingo(winningBingo, lastNumCalled);
    }


    static int partB(Scanner fileReader) {
        // Reading the first numbers
        String firstLine = fileReader.nextLine();
        String[] strNumbers = firstLine.split(",");
        int[] intNumbers = new int[strNumbers.length];
        for (int i = 0; i < strNumbers.length; i++) {
            intNumbers[i] = Integer.parseInt(strNumbers[i]);
        }

        ArrayList<ElementBingo[][]> allBingos = new ArrayList<ElementBingo[][]>();

        // Filling each matrix
        int idx = 0;
        while (fileReader.hasNext())  {
            ElementBingo[][] currentBingo = new ElementBingo[5][5];
            for (int i = 0; i < 5; i++) {
                for (int j = 0; j < 5; j++) {
                    currentBingo[i][j] = new ElementBingo(fileReader.nextInt());
                }
            }
            allBingos.add(idx, currentBingo);
            idx += 1;
        }

        // Finding the last bingo to win
        int lastNumCalled = intNumbers[0];
        ElementBingo[][] winningBingo = null;
        for (int i = 0; i < intNumbers.length; i++) {
            lastNumCalled = intNumbers[i];
            markNumberVisited(allBingos, lastNumCalled);
            while ((winningBingo = getWinningBingo(allBingos)) != null && allBingos.size() != 1) {
                // It may be the case that more than one bingo win at the same time. For this reason, we have to remove all the winning bingos each time.
                allBingos.remove(winningBingo);
            }
            if (winningBingo != null && allBingos.size() == 1) {
                // If we have a winning  bingo and it is the last in the list, we have to stop playing.
                break;
            }
        }

        return getScoreBingo(winningBingo, lastNumCalled);
    }

    public static void main(String[] args) {
        try {
            String dataPath = "Day4/day4_data.txt";
            //String examplePath = "Day4/day4_example.txt";
            File inputData = new File(dataPath);
            //File inputData = new File(examplePath);
            Scanner fileReaderA = new Scanner(inputData);
            Scanner fileReaderB = new Scanner(inputData);
            
            
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