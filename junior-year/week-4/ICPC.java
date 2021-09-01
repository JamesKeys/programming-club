// Written by Jim Keys at Villanova University
// Solves Kattis problem found here: https://open.kattis.com/problems/tutorial

import java.util.Scanner;

public class ICPC {
   public static long fact(long x) {
      // Calculates the factorial of x and returns it
      if (x == 1)
         return 1;
      return x*fact(x-1);
   }
   public static void main(String args[]) {
      Scanner scan = new Scanner(System.in); // Takes input
      
      long maxOperations = scan.nextInt(); // Max Operations allowed in the time limit
      long maxInput = scan.nextInt(); // The n in big O notation, ex. O(n) or O(n*log(n))
      int complexity = scan.nextInt(); // The complexity of the algorithm to be run
      long operations = 0; // This is how many operations will be run by an algorithm with this complexity and this n
      
      switch (complexity) {
         case 1: 
            // This check filters to make sure we don't unnecessarily run a recursive function
            if (Math.pow(2, maxInput) > maxOperations)
               operations = maxOperations+1;
            else
               operations = fact(maxInput); // O(n!)
            break;
         case 2:
            operations = (long)Math.pow(2, maxInput); // O(2^n)
            break;
         case 3:
            operations = (long)Math.pow(maxInput, 4); // O(n^4)
            break;
         case 4:
            operations = (long)Math.pow(maxInput, 3); // O(n^3)
            break;
         case 5:
            operations = (long)Math.pow(maxInput, 2); // O(n^2)
            break;
         case 6:
            operations = (long)(maxInput*(Math.log(maxInput)/Math.log(2))+0.5); // O(n*log2(n))
            break;
         case 7:
            operations = maxInput; // O(n)
      }
      if (operations > maxOperations)
         System.out.println("TLE"); // Time Limit Exceeded
      else
         System.out.println("AC"); // Accepted
   }
}