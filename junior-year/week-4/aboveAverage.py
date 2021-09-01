# Created by Jim Keys at Villanova University
# Solves Kattis problem found at https://open.kattis.com/problems/aboveaverage

numCases = int(input())

for case in range(numCases):
	line = input().split() # This has the entire line, starting with the number of grades to follow
	numStudents = int(line[0])

	grades = line[1:] # Get the line without the number of students
	grades = [int(i) for i in grades] # Cast from strings to integers
	
	aboveAvg = [x > (sum(grades)/numStudents) for x in grades] # Boolean array of above average scores
	
	ans = (str(round(sum(aboveAvg)/numStudents*100, 3)) + "00")[0:6]+"%" # Number of above averages to 3 decimal places
	print(ans)