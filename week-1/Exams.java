import java.util.Scanner;

class Exams {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        int numCorrect = Integer.parseInt(scan.nextLine());
        String friendAns = scan.nextLine();
        String myAns = scan.nextLine();
        int numQuestions = friendAns.length();
        int numIncorrect = numQuestions-numCorrect;
        int numMatching = 0;
        
        for(int i = 0; i < numQuestions; i++) {
            if(friendAns.substring(i,i+1).equals(myAns.substring(i,i+1)))
                numMatching++;
        }
        int numPossible;
        if(numMatching < numCorrect) {
            numPossible = numMatching + (numQuestions-numCorrect);
        } else {
            numPossible = numCorrect + (numQuestions-numMatching);
        }
        
        System.out.println(numPossible);
    }
}