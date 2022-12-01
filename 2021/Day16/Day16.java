package Day16;

import java.util.*;

import java.io.*;


public class Day16 {
    private static HashMap<String, String> hexDecimalMap;
    public static final int GROUP_LENGTH = 5;

    static void initHashMap() {
        hexDecimalMap = new HashMap<String, String>();
        hexDecimalMap.put("0", "0000");
        hexDecimalMap.put("1", "0001");
        hexDecimalMap.put("2", "0010");
        hexDecimalMap.put("3", "0011");
        hexDecimalMap.put("4", "0100");
        hexDecimalMap.put("5", "0101");
        hexDecimalMap.put("6", "0110");
        hexDecimalMap.put("7", "0111");
        hexDecimalMap.put("8", "1000");
        hexDecimalMap.put("9", "1001");
        hexDecimalMap.put("A", "1010");
        hexDecimalMap.put("B", "1011");
        hexDecimalMap.put("C", "1100");
        hexDecimalMap.put("D", "1101");
        hexDecimalMap.put("E", "1110");
        hexDecimalMap.put("F", "1111");
    }

    static int binaryToDecimal(String binaryNumber) {
        int binary = 0;
        for (int i = binaryNumber.length() - 1; i >= 0; i--) {
            int number = Integer.parseInt(String.valueOf(binaryNumber.charAt(i)));
            double power = Math.pow(2, binaryNumber.length() - i - 1);
            binary += number * power;
        }
        return binary;
    }

    static int processPacket(String packet) {
        String dataPart = packet.substring(6);
        String currentGroup = "";
        String value = "";
        int idx = 0;
        do {
            currentGroup = dataPart.substring(0, GROUP_LENGTH);
            currentGroup = dataPart.substring(idx, idx + GROUP_LENGTH);
            idx += GROUP_LENGTH;
            value += currentGroup.substring(1, GROUP_LENGTH);
        } while (String.valueOf(currentGroup.charAt(0)).equals("0") == false);
        
        return binaryToDecimal(value);
    }
    
    static int partA(Scanner fileReader) {
        String inputLine = fileReader.nextLine();
        String binaryRepresentation = "";
        for (int i = 0; i < inputLine.length(); i++) {
            // Transforming from hexadecimal to binary
            binaryRepresentation += hexDecimalMap.get(String.valueOf(inputLine.charAt(i)));
        }
        int version = binaryToDecimal(binaryRepresentation.substring(0, 3));
        int id = binaryToDecimal(binaryRepresentation.substring(3, 6));
        System.out.println("Version: " + version);
        System.out.println("Id: " + id);
        if (id == 4) {
            int value = processPacket(binaryRepresentation);
        } else {
            char lengthTypeId = binaryRepresentation.charAt(6);
            System.out.println(lengthTypeId);
            if (String.valueOf(lengthTypeId).equals("0")) {
                String lengthSubpackets = binaryRepresentation.substring(7, 7 + 15);
                System.out.println("length subpackets = " + lengthSubpackets);
            } else {
                int numberSubpackets = binaryToDecimal(binaryRepresentation.substring(7, 7 + 11));
                System.out.println(binaryRepresentation.substring(18).length() % numberSubpackets);
            }
            
        }
        return 0;
    }

    

    static int partB(Scanner fileReader) {
        return 0;
    }

    public static void main(String[] args) {
        try {
            //String dataPath = "Day16/day16_data.txt";
            String examplePath = "Day16/day16_example.txt";
            Scanner fileReaderA = new Scanner(new File(examplePath));
            Scanner fileReaderB = new Scanner(new File(examplePath));
            
            initHashMap();
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