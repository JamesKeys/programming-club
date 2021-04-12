# Created by Jim Keys at Villanova University
# Solves Kattis problem found here: https://open.kattis.com/problems/schoolspirit

def calcScores(individualScores): # Calculates the team score according to the ICPC scoring system
	sum = 0
	for i in range(len(individualScores)):
		sum += 0.2*individualScores[i]*(0.8**i)
	return sum
	
def removeIthScore(individualScores, iToRemove): # Removes the i'th participant from the 
						 # array and returns new array of individual scores
	retVal = []
	for i in range(len(individualScores)):
		if i != iToRemove:
			retVal.append(individualScores[i])
	return retVal


numStudents = int(input())
individualScores = [] # Holds the individual scores of the team

for i in range(numStudents):
	individualScores.append(int(input()))

newTeamScores = [] # Holds the team score if the i'th player left the team
for i in range(numStudents):
	newArray = removeIthScore(individualScores, i)
	newScore = calcScores(newArray)
	newTeamScores.append(newScore)

print(calcScores(individualScores)) # Current team score
print(sum(newTeamScores)/numStudents) # Average of possible new team scores