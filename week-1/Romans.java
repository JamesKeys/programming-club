import java.util.Scanner;

class Romans {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        double userIn = scan.nextDouble();
        
        int userOut = (int)(userIn*1000*5280/4854+0.5);
        System.out.println(userOut);
    }
}