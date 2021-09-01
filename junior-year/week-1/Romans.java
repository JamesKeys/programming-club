// Written by Jim Keys at Villanova University
// Solving Kattis problem found here: https://open.kattis.com/problems/romans

import java.util.Scanner;

class Romans {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in); // Scanner reads input
        double milesIn = scan.nextDouble(); // Reads how many miles to convert to roman paces
        
        int romanStepsOut = (int)(milesIn*1000*5280/4854+0.5); // Uses equation given, adding 0.5 and truncating to round 0.5+ up, and 0.0-0.49 down
        System.out.println(romanStepsOut);
    }
}