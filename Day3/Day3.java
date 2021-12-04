package Day3;

import java.util.*;


import java.io.*;

public class Day3 {
    static int binaryToDecimal(String str) {
        int result = 0;
        int strLength = str.length();

        for (int i = 0; i < strLength; i++) {
            result += Integer.parseInt(String.valueOf(str.charAt(strLength - i - 1))) * Math.pow(2, i);
        }

        return result;
    }


    static int partA(Scanner fileReader, int lengthLines) {
        String gammaRate = "";
        String epsilonRate = "";
        int[] zeroCount = new int[lengthLines];
        int numberLines = 0;

        while (fileReader.hasNext()) {
            String currentStr = fileReader.nextLine();
            for (int i = 0; i < currentStr.length(); i++) {
                if (Character.compare('0', currentStr.charAt(i)) == 0) {
                    zeroCount[i] += 1;
                }
            }
            numberLines += 1;
        }

        for (int i = 0; i < lengthLines; i++) {
            if (zeroCount[i] > numberLines / 2) {
               gammaRate += "0";
               epsilonRate += "1";
            } else {
                gammaRate += "1";
                epsilonRate += "0";
            }
        }

        return binaryToDecimal(gammaRate) * binaryToDecimal(epsilonRate);
    }

    static int[] countZeroFreq(LinkedList<String> list) {
        int[] zeros = new int[list.get(0).length()];
        for (int i = 0; i < list.size(); i++) {
            String currentStr = list.get(i);
            for (int j = 0; j < currentStr.length(); j++) {
                if (Character.compare('0', currentStr.charAt(j)) == 0) {
                    zeros[j] += 1;
                }
            }
        }

        return zeros;
    }


    static int partB(Scanner fileReader, int lengthLines) {
        int[] zeroCount = new int[lengthLines];
        LinkedList<String> oxygenList = new LinkedList<String>();
        LinkedList<String> co2List = new LinkedList<String>();
        int numberLines = 0;

        // Filling both lists with all the strings in the txt file
        while (fileReader.hasNext()) {
            String currentStr = fileReader.nextLine();
            oxygenList.add(currentStr);
            co2List.add(currentStr);
            numberLines += 1;
        }

        // Applying the conditions to obtain the O2 rate.
        int tmpNumLines = numberLines;
        int idxToCompare = 0;
        while (oxygenList.size() != 1) {
            int currentTotalLines = tmpNumLines;
            zeroCount = countZeroFreq(oxygenList); // Every time that we remove an element, we have to recalculate the frequencies of zeros and ones in the remaining elements
            for (int i = 0; i < oxygenList.size(); i++) {
                if (zeroCount[idxToCompare] > currentTotalLines / 2) {
                    if (Character.compare('1', oxygenList.get(i).charAt(idxToCompare)) == 0) {
                        oxygenList.remove(i);
                        i -= 1;
                        tmpNumLines -= 1;
                    }
                } else if (zeroCount[idxToCompare] <= currentTotalLines / 2) {
                    if (Character.compare('0', oxygenList.get(i).charAt(idxToCompare)) == 0) {
                        oxygenList.remove(i);
                        i -= 1;
                        tmpNumLines -= 1;
                    }
                }
            }
            idxToCompare += 1;
        }

        // Applying the conditions to obtain the CO2 rate
        tmpNumLines = numberLines;
        idxToCompare = 0;
        while (co2List.size() != 1) {
            int currentTotalLines = tmpNumLines;
            zeroCount = countZeroFreq(co2List); // As before, every time that we remove an element, we have to recompute the new frequencies
            for (int i = 0; i < co2List.size(); i++) {
                if (zeroCount[idxToCompare] <= currentTotalLines / 2) {
                    if (Character.compare('1', co2List.get(i).charAt(idxToCompare)) == 0) {
                        co2List.remove(i);
                        i -= 1;
                        tmpNumLines -= 1;
                    }
                } else if (zeroCount[idxToCompare] > currentTotalLines / 2) {
                    if (Character.compare('0', co2List.get(i).charAt(idxToCompare)) == 0) {
                        co2List.remove(i);
                        i -= 1;
                        tmpNumLines -= 1;
                    }
                }
            }
            idxToCompare += 1;
        }

        return binaryToDecimal(oxygenList.get(0)) * binaryToDecimal(co2List.get(0));
    }

    public static void main(String[] args) {
        try {
            String dataPath = "Day3/day3_data.txt";
            //String examplePath = "Day3/day3_example.txt";
            File inputData = new File(dataPath);
            //File inputData = new File(examplePath);
            Scanner fileReaderA = new Scanner(inputData);
            Scanner fileReaderB = new Scanner(inputData);
            int lengthLineData = 12;
            //int lengthLineExample = 5;
            
            // Example
            //System.out.println("Final result part a: " + partA(fileReaderA, lengthLineExample));
            
            // Data
            System.out.println("Final result part a: " + partA(fileReaderA, lengthLineData));
            fileReaderA.close();
            System.out.println("Final result part b: " + partB(fileReaderB, lengthLineData));
            fileReaderB.close();

        } catch (FileNotFoundException e) {
            System.out.println("The file could not be found");
            e.printStackTrace();
        }
    }
}