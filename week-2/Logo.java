// Written by Jim Keys at Villanova University
// Solves Logo problem on Kattis at: https://open.kattis.com/problems/logo

import java.util.Scanner;

public class Logo {
	// This program takes inputs concerning a path, including turning left or right x degrees,
	// and moving forward and backward y units. Outputs the distance from the starting location in units.
	
	
	public static double[] calcNewCoordinates(double[] currCoordinates, int currDirection, int toMove) {
		/* INPUT
			double[] currCoordinates: Array containing x and y coordinates in positions 0 and 1
			int currDirection: Degree value, 0 degrees being right, 90 up, 180 left, 270 down
			int toMove: distance to move in units
			
			OUTPUT
			double[] newCoordinates: Array containing x and y coordinates in positions 0 and 1
		*/
		double xVal = currCoordinates[0];
		double yVal = currCoordinates[1];
		
		double newXVal = xVal + Math.cos(Math.toRadians(currDirection))*toMove; // cosine = adjacent/hypotenuse = x_units_traveled/straight_units_traveled
		double newYVal = yVal + Math.sin(Math.toRadians(currDirection))*toMove; // sine = opposite/hypotenuse = y_units_traveled/straight_units_traveled
		
		double[] newCoordinates = new double[]{ newXVal, newYVal };
		
		return newCoordinates;
	}
	
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int numTestCases = scan.nextInt(); scan.nextLine();
		
		for(int i = 0; i < numTestCases; i++) {
			int numCommands = scan.nextInt(); scan.nextLine();
			double[] coordinates = new double[]{ 0.0,0.0 }; // This holds the x and y coordinates of the "turtle"
			
			int facing = 0; // in degrees, 0 = right, 90 = up, 180 = left, 270 = down
			
			for(int x = 0; x < numCommands; x++) {
				String newDirection = scan.next();
 				if(newDirection.equals("lt")) {
					facing = (facing + scan.nextInt()) % 360;
					scan.nextLine();
				} else if(newDirection.equals("rt")) {
					int degrees = scan.nextInt();
					if(facing - degrees < 0)
						facing = 360 + (facing - degrees);
					else
						facing = facing - degrees;
					scan.nextLine();
				} else if(newDirection.equals("fd")) {
					coordinates = calcNewCoordinates(coordinates, facing, scan.nextInt());
					scan.nextLine();
				} else if(newDirection.equals("bk")) { // backwards is just forwards in the opposite direction
					coordinates = calcNewCoordinates(coordinates, (facing+180)%360, scan.nextInt());
					scan.nextLine();
				}
			}
			// distance from start is calculated using pythagorean theorem, rounded to nearest integer
			System.out.println((int)(Math.sqrt(Math.pow(coordinates[0],2)+Math.pow(coordinates[1],2))+0.5));
		}
	}
}