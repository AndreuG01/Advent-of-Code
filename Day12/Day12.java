package Day12;

import java.util.*;

import java.io.*;


class Node {
    private String content;
    private boolean visited;
    private List<Node> next;

    public Node(String content) {
        this.content = content;
        visited = false;
        next = new ArrayList<Node>();
    }
    public String getContent() { return content; }

    public boolean isVisited() { return visited; }
    public void setVisited() { visited = true; }
    public void appendChild(Node childNode) {
        next.add(childNode);
    }
    public boolean isBig() {
        return content.toUpperCase().compareTo(content) == 0;
    }
    public boolean isStart() {
        return content.compareTo("start") == 0;
    }
}
class Tree {
    private Node head;

    public Tree(Node head) {
        this.head = head;
    }
}

public class Day12 {
    
    static int partA(Scanner fileReader) {
        // It is a good idea to build a tree and then perform a Depth Search First
        Node startNode = null;
        Tree tree = null;
        Map<String, Node> allNodes = new HashMap<String, Node>();
        while (fileReader.hasNext()) {
            String currentLine = fileReader.nextLine();
            String[] content = currentLine.split("-");
            Node node1 = new Node(content[0]);
            Node node2 = new Node(content[1]);
            node1.appendChild(node2);
            node2.appendChild(node1);
            if (allNodes.containsKey(node1.getContent())) {
                allNodes.get(node1.getContent()).appendChild(node2);
            } else {
                allNodes.put(node1.getContent(), node1);
            }
            if (allNodes.containsKey(node2.getContent())) {
                allNodes.get(node2.getContent()).appendChild(node1);
            } else {
                allNodes.put(node2.getContent(), node2);
            }

        }
        return 0;
    }

    static int partB(Scanner fileReader) {
        return 0;
    }

    public static void main(String[] args) {
        try {
            //String dataPath = "Day12/day12_data.txt";
            String examplePath = "Day12/day12_example.txt";
            Scanner fileReaderA = new Scanner(new File(examplePath));
            Scanner fileReaderB = new Scanner(new File(examplePath));
            
            
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