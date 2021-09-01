// Written by Jim Keys at Villanova University
// Solves Kemija from Kattis found here: https://open.kattis.com/problems/kemija08

import java.util.*;

public class Kemija
{
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in); // Retrieves input
		
		String sentence = scan.nextLine();
		String decodedSentence = "";

		for(int i = 0; i < sentence.length(); i++) {
		// iteratively moves through input to remove the extra two characters
			decodedSentence = decodedSentence + sentence.substring(i,i+1);
			if(sentence.substring(i,i+1).equals("a") || sentence.substring(i,i+1).equals("e") || sentence.substring(i,i+1).equals("i") || sentence.substring(i,i+1).equals("o") || sentence.substring(i,i+1).equals("u"))
				i = i + 2;
				// If the current character is a vowel, skip the next two characters
		}
		System.out.println(decodedSentence);
	}
}