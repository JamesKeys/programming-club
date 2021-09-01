// Written by Jim Keys from Villanova University
// Solving Kattis problem found here: https://open.kattis.com/problems/recount

import java.util.Scanner;
import java.util.HashMap;

public class Recount {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in); // Scanner takes input
		HashMap<String, int> recount = new HashMap<String, int>(); 
      // HashMap with keys of Strings representing the name of the candidate and
      // a value of Integer consisting of the number of votes cast for them.
		
      // This counts all the votes, until there are no more lines remaining
		while (scan.hasNextLine()) {
			String vote = scan.nextLine();
         // Stores the vote at the current line and advances scanner head
			
			if (recount.containsKey(vote))
				recount.put(vote, recount.get(vote)+1); // Increments value for candidate
			else
				recount.put(vote, 1); // Adds new candidate to HashMap
		}
		
		String maxName = ""; // Tracker for the current leader
		int maxVotes = -1; // Tracker for the current max votes
		boolean isRunoff = false; // Boolean value to keep track if there is currently a tie
		
      // Loops through all the keys, compares values
		for(String key : recount.keySet()) {
			if (recount.get(key) > maxVotes) { // If there is a new leader, update max values, no tie anymore
				maxName = key;
				maxVotes = recount.get(key);
				isRunoff = false;
			} else if (recount.get(key) == maxVotes) { // If there is now a tie, update isRunoff to true
				isRunoff = true;
			}
		}
		
      // Print output
		if(isRunoff)
			System.out.println("Runoff!");
		else
			System.out.println(maxName);
	}
}