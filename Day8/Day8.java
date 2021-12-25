package Day8;

import java.util.*;

import java.io.*;

public class Day8 {
    public static final int LENGTH1 = 2;
    public static final int LENGTH4 = 4;
    public static final int LENGTH7 = 3;
    public static final int LENGTH8 = 7;



    static int partA(Scanner fileReader) {
        int counter = 0;
        while (fileReader.hasNext()) {
            String[] output = fileReader.nextLine().split("\\|")[1].split(" ");
            // We have to iterate over the output and determine the number of times that 1, 4, 7, or 8 appears
            for (String currentOutput : output) {
                int length = currentOutput.length();
                if (length == LENGTH1 || length == LENGTH4 || length == LENGTH7 || length == LENGTH8) {
                    counter += 1;
                }
            }
        }
        return counter;
        
    }

    static String charArrayToString(char[] array) {
        String output = "";
        for (int i = 0; i < array.length; i++) {
            output += array[i];
        }
        return output;
    }

    static boolean stringContainsChar(String str, char character) {
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == character) {
                return true;
            }
        }
        return false;
    }

    static String findThree(List<String> fiveLengthNumbers, String one) {
        for (String currentString : fiveLengthNumbers) {
            if (stringContainsChar(currentString, one.charAt(0)) && stringContainsChar(currentString, one.charAt(1))) {
                return currentString;
            }
        }
        return null;
    }

    static String findFive(List<String> fiveLengthNumbers, String four) {
        // Given a 4, if the number of matches in a five length number is 3, then the number is a five
        for (String currenString : fiveLengthNumbers) {
            int numberMathces = 0;
            for (int i = 0; i < four.length(); i++) {
                if (stringContainsChar(currenString, four.charAt(i))) {
                    numberMathces += 1;
                }
            }
            if (numberMathces == 3) {
                return currenString;
            }
        }
        return null;
    }

    static String findSix(List<String> sixLengthList, String seven) {
        // Given a 7, if the number of matches is different than 3, then the number is a 6
        for (String currentString : sixLengthList) {
            int numberMathces = 0;
            for (int i = 0; i < seven.length(); i++) {
                if (stringContainsChar(currentString, seven.charAt(i))) {
                    numberMathces += 1;
                }
            }
            if (numberMathces != 3) {
                return currentString;
            }
        }
        return null;
    }

    static String findNine(List<String> sixLengthList, String four) {
        // If the number of matches is 4, then we have found the number 9
        for (String currentString : sixLengthList) {
            int numberMatches = 0;
            for (int i = 0; i < four.length(); i++) {
                if (stringContainsChar(currentString, four.charAt(i))) {
                    numberMatches += 1;
                }
            }
            if (numberMatches == 4) {
                return currentString;
            }
        }

        return null;
    }

    static String sortString(String str) {
        char[] charArray = str.toCharArray();
        Arrays.sort(charArray);
        return charArrayToString(charArray);
    }

    static int partB(Scanner fileReader) {
        // Initializing the map with the numbers
        int totalResult = 0;
        while (fileReader.hasNextLine()) {
            String[] inputOutput = fileReader.nextLine().split("\\|");
            String[] input = inputOutput[0].split(" ");
            String[] output = inputOutput[1].split(" ");
            
            Map<String, Integer> map = new HashMap<String, Integer>(); // The sorted string and the number that it represents will be stored here.
            List<String> fiveLengthList = new ArrayList<String>(); // The representation of 2, 3, 5 will be stored here.
            List<String> sixLengthList = new ArrayList<String>(); // The representation of 0, 6, 9 will be stored here.
            String[] numbers = new String[10]; // Array where all the number representations will be stored.
            
            for (int i = 0; i < input.length; i++) {
                String currentString = input[i];
                String sortedString = sortString(currentString);

                // Filling the map with the numbers that can be known directly and storing the others in their corresponding array.
                if (input[i].length() == LENGTH1) {
                    numbers[1] = sortedString;
                    map.put(sortedString, 1);
                } else if (input[i].length() == LENGTH4) {
                    numbers[4] = sortedString;
                    map.put(sortedString, 4);
                } else if (input[i].length() == LENGTH7) {
                    numbers[7] = sortedString;
                    map.put(sortedString, 7);
                } else if (input[i].length() == LENGTH8) {
                    numbers[8] = sortedString;
                    map.put(sortedString, 8);
                } else if (input[i].length() == 5) {
                    fiveLengthList.add(input[i]);
                } else {
                    sixLengthList.add(input[i]);
                }
            }

            // If we have the combinations that produce a 1, 4, 7 and 8, we can obtain the rest of the numbers.

            // Given a 1 and 2, 3, 5, we can know which combination produces the number 3
            String number3 = findThree(fiveLengthList, numbers[1]);
            numbers[3] = sortString(number3);
            fiveLengthList.remove(number3);

            // Given a 4 and 2, 3, 5, we can know which combination produces the number 5
            String number5 = findFive(fiveLengthList, numbers[4]);
            numbers[5] = sortString(number5);
            fiveLengthList.remove(number5);

            // The remaining number is the 2
            numbers[2] = sortString(fiveLengthList.get(0));

            // Given a 7 and 0, 6, 9, we can know which combination produces the number 6
            String number6 = findSix(sixLengthList, numbers[7]);
            numbers[6] = sortString(number6);
            sixLengthList.remove(number6);

            // Given a 4 and 0, 9, we can know which combination produces the number 9
            String number9 = findNine(sixLengthList, numbers[4]);
            numbers[9] = sortString(number9);
            sixLengthList.remove(number9);

            // The remaining number is the 0
            numbers[0] = sortString(sixLengthList.get(0));

            // Once we have all the numbers, we can put them in the map to later get the values of the output immediately.
            for (int i = 0; i < numbers.length; i++) {
                map.put(numbers[i], i);
            }

            // Processing the output
            String currentStringNumber = "";
            for (int i = 0; i < output.length; i++) {
                try {
                    currentStringNumber +=  map.get(sortString(output[i])).toString();
                } catch (Exception e) {
                }
            }

            totalResult += Integer.parseInt(currentStringNumber);
        }
        
        return totalResult;
    }

    public static void main(String[] args) {
        try {
            String dataPath = "Day8/day8_data.txt";
            //String examplePath = "Day8/day8_example.txt";
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