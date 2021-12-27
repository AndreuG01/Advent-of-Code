package Day10;

import java.util.*;

import java.io.*;
import java.math.BigInteger;

public class Day10 {
    static int characterScore(Character character) {
        if (character.compareTo(')') == 0) {
            return 3;
        } else if (character.compareTo(']') == 0) {
            return 57;
        } else if (character.compareTo('}') == 0) {
            return 1197;
        } else if (character.compareTo('>') == 0) {
            return 25137;
        }
        return 0;
    }
    
    static int partA(Scanner fileReader) {
        int totalScore = 0;
        while (fileReader.hasNext()) {
            Stack<Character> stack = new Stack<Character>();
            String currentLine = fileReader.nextLine();
            int currentLineLength = currentLine.length();
            for (int i = 0; i < currentLineLength; i++) {
                Character currentChar = currentLine.charAt(i);
                if (currentChar.compareTo('[') == 0 || currentChar.compareTo('(') == 0 || currentChar.compareTo('{') == 0 || currentChar.compareTo('<') == 0) {
                    // If the character is not a closing character, push it to the stack.
                    stack.push(currentChar);
                } else {
                    Character topCharacter = stack.pop(); // Retrieve the top character
                    if ((currentChar.compareTo(']') == 0 && topCharacter.compareTo('[') != 0) || (currentChar.compareTo(')') == 0 && topCharacter.compareTo('(') != 0) || (currentChar.compareTo('}') == 0 && topCharacter.compareTo('{') != 0) || (currentChar.compareTo('>') == 0 && topCharacter.compareTo('<') != 0)) {
                        // If the top character does not close a chunk, we have to get the score associated to it.
                        totalScore += characterScore(currentChar);
                        break;
                    }
                }
            }
        }

        return totalScore;
    }

    static boolean lineIsCorrupted(String line) {
        Stack<Character> stack = new Stack<Character>();
        int lineLength = line.length();
        for (int i = 0; i < lineLength; i++) {
            Character currentChar = line.charAt(i);
            if (currentChar.compareTo('[') == 0 || currentChar.compareTo('(') == 0 || currentChar.compareTo('{') == 0 || currentChar.compareTo('<') == 0) {
                // If the character is not a closing character, push it to the stack.
                stack.push(currentChar);
            } else {
                Character topCharacter = stack.pop(); // Retrieve the top character
                if ((currentChar.compareTo(']') == 0 && topCharacter.compareTo('[') != 0) || (currentChar.compareTo(')') == 0 && topCharacter.compareTo('(') != 0) || (currentChar.compareTo('}') == 0 && topCharacter.compareTo('{') != 0) || (currentChar.compareTo('>') == 0 && topCharacter.compareTo('<') != 0)) {
                    // If the top character does not close a chunk, then the line is not correct.
                    return true;
                }
            }
        }

        return false;
    }

    static Character getClosingCharacter(Character character) {
        if (character.compareTo('[') == 0) {
            return ']';
        } else if (character.compareTo('(') == 0) {
            return ')';
        } else if (character.compareTo('<') == 0) {
            return '>';
        } else if (character.compareTo('{') == 0) {
            return '}';
        }
        return null;
    }

    static BigInteger getScore(String str) {
        BigInteger totalScore = BigInteger.valueOf(0);
        for (int i = 0; i < str.length(); i++) {
            int charScore = 0;
            Character character = str.charAt(i);
            if (character.compareTo(']') == 0) {
                charScore = 2;
            } else if (character.compareTo(')') == 0) {
                charScore = 1;
            } else if (character.compareTo('>') == 0) {
                charScore = 4;
            } else if (character.compareTo('}') == 0) {
                charScore = 3;
            }
            totalScore = totalScore.multiply(BigInteger.valueOf(5));
            totalScore = totalScore.add(BigInteger.valueOf(charScore));
        }
        return totalScore;
    }

    static BigInteger partB(Scanner fileReader) {
        List<BigInteger> scoreList = new ArrayList<BigInteger>();
        BigInteger midScore = new BigInteger("0");
        while (fileReader.hasNext()) {
            Stack<Character> stack = new Stack<Character>();
            String currentString = fileReader.nextLine();
            if (lineIsCorrupted(currentString) == false) {
                int currentLength = currentString.length();
                for (int i = 0; i < currentLength; i++) {
                    Character currentChar = currentString.charAt(i);
                    if (currentChar.compareTo('[') == 0 || currentChar.compareTo('(') == 0 || currentChar.compareTo('{') == 0 || currentChar.compareTo('<') == 0) {
                        stack.push(currentChar);
                    } else {
                        stack.pop();
                    }
                }
                // At this point, we have to take the remaining characters in the stack and produce the combination of the closing characters
                int stackSize = stack.size();
                String closingCombination = "";
                for (int i = 0; i < stackSize; i++) {
                    closingCombination += "" + getClosingCharacter(stack.pop());
                }
                
                // Once we have the closing combination, we can get the score from it and store it into the array
                scoreList.add(getScore(closingCombination));
            }
            // Once we have all the scores, we can sort them
            Collections.sort(scoreList);
            // Get the middle element
            midScore = scoreList.get(scoreList.size() / 2);
        }
        return midScore;
    }

    public static void main(String[] args) {
        try {
            String dataPath = "Day10/day10_data.txt";
            //String examplePath = "Day10/day10_example.txt";
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