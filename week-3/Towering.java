// Written by Jim Keys at Villanova University
// Solves Kattis problem found here: https://open.kattis.com/problems/towering

import java.util.*;

public class Towering
{
    public static int[][] calcCombinations(int[] arr) {
	// INPUT: array to calculate combinations of, length=6, length of combinations=3
	// OUTPUT: 2d array of dimensions 20x3 containing all combinations of size 3
        int[][] retVal = new int[20][3];
        int index = 0;
        
        for(int j = 0; j < 4; j++) { // First value
            for(int i = j+1; i < 5; i++) { // Second value
                for(int m = i+1; m < 6; m++) { // Third value
                    retVal[index][0] = arr[j];
                    retVal[index][1] = arr[i];
                    retVal[index][2] = arr[m];
                    index++;
                }
            }
        }
        return retVal;
    }
    
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in); // Used to take input
        int[] boxes = new int[6]; // Holds the height value for the six boxes
        
        for(int i = 0; i < 6; i++)
            boxes[i] = -1*scan.nextInt(); // Stored negatively initially for sorting
        
        Arrays.sort(boxes, 0, 6); // Knew this sorted ascending, didn't want to write out my own sorting
        for(int i = 0; i < 6; i++) // So I sorted ascending, negatively, then swapped them back to
            boxes[i] = -1*boxes[i]; // their original values to get descending values
        
        int height1 = scan.nextInt(); // First height to configure boxes to be
        int height2 = scan.nextInt(); // Second height to configure boxes
        
        int[][] combinations = calcCombinations(boxes);
        
        for(int[] arr : combinations) {
            int sum = 0;
            for(int element : arr)
                sum += element;
            if(sum == height1) // If this combination yields the correct height
            {
                for(int element : arr)
                    System.out.print(element + " ");
            }
        }
        for(int[] arr : combinations) {
            int sum = 0;
            for(int element : arr)
                sum += element;
            if(sum == height2) // If this combination yields the correct height
            {
                for(int element : arr)
                    System.out.print(element + " ");
            }
        }
    }
}