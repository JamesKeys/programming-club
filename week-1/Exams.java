// Written by Jim Keys from Villanova University
// Solving Kattis problem found here: https://open.kattis.com/problems/exam

import java.util.Scanner;

class Exams {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in); // Scanner takes input
        
        int numCorrect = Integer.parseInt(scan.nextLine()); // Integer to record the number of answers "my friend" got correct
        String friendAns = scan.nextLine(); // String of T/F answers from "my friend"s exam - ex: TFTTTTF
        String myAns = scan.nextLine(); // String of T/F answers from my exam - ex: FTTTTTF
        int numQuestions = friendAns.length();
        int numMatching = 0;
        
        // Loop to iterate over each character, comparing my answers to "my friend"s answers and incrementing the tracker
        for(int i = 0; i < numQuestions; i++) {
            if(friendAns.substring(i,i+1).equals(myAns.substring(i,i+1)))
                numMatching++;
        }
        
        // OUTPUT value showing the maximum number of questions I can get right based off the known variables
        int numPossible;
        
        // LOGICAL : I assume that each matching answer is correct, until we either:
                  // A: Run out of matching answers: They have more correct answers left, however many correct are left, I got wrong, and the rest I got right.
                  // B: Run out of correct answers: The rest of our matches are wrong, and I got all the unmatched correct.
                  
        // MATHEMATICAL : See below
        numPossible = numQuestions - Math.abs(numMatching-numCorrect);
        System.out.println(numPossible);
    }
}