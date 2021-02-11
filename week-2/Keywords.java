// Written by Jim Keys at Villanova University
// Solves Keywords on Kattis here: https://open.kattis.com/problems/keywords

import java.util.Scanner;
import java.util.Arrays;

public class Keywords {
	// This project takes n keywords from input and outputs the number of 
	// identical words not involving capitalization or using hyphens instead of spaces

	// ex. Machine-Learning = machine learning

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in); // scanner used to take input
		
		int numInputs = scan.nextInt();
		scan.nextLine();
		String[] phrases = new String[numInputs]; // This holds all the inputs
		
		// This populates the array that holds all the inputs
		for(int i = 0; i < numInputs; i++) {
			phrases[i] = scan.nextLine();
			phrases[i] = phrases[i].replace("-", " ").toLowerCase(); // immediately converts hyphens to spaces and lowercases
		}
		
		Arrays.sort(phrases, 0, phrases.length); // This sorts the array, forcing all duplicates to be back-to-back
		int numUnique = 0; // running total
		String lastVal= ""; // saves the previous value, since any duplicates will be together

		// This runs through the array, incrementing numUnique if the previous value does not match the current value in the array
		for(int i = 0; i < phrases.length; i++) {
			if(!phrases[i].equals(lastVal)) {
				numUnique++;
				lastVal = phrases[i];
			}
		}
		System.out.println(numUnique);
	}
}