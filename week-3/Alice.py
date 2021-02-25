# Written by Jim Keys at Villanova University
# Solves problem from Kattis at: https://open.kattis.com/problems/alicedigital

def sum(arr, beg, end):
	# INPUT: int[] arr = array to sum numbers, starting at i = int beg, and ending at i = int end
	# OUTPUT: int sum of values

	sumVal = 0
	for i in range(beg, end+1, 1):
		sumVal += arr[i]
	return sumVal
	
def findBounds(arr, index, minVal):
	# INPUT: int[] arr = array to use, getting bounds from i = int index, using int minVal as the
		# number to make sure all values in bounds are greater than
	# OUTPUT: int lowerBound, int upperBound inclusive of indices to sum for weight with int minVal
		# as the lowest value between the bounds

	lowerBound, upperBound = index, index
	while(lowerBound > 0 and arr[lowerBound-1] > minVal):
		lowerBound -= 1
	while(upperBound < len(arr)-1 and arr[upperBound+1] > minVal):
		upperBound += 1

	return lowerBound, upperBound


numDatasets = int(input())


for rounds in range(numDatasets):
	numInts, minVal = input().split()
	numInts, minVal = int(numInts), int(minVal)
	
	values = input().split()
	occurences = [] # This array keeps track of the instances of the minimum desired value
	
	for i in range(numInts):
		values[i] = int(values[i])
		if (values[i] == minVal):
			occurences.append(i) # After converting to int, compare to see if the i'th
						# value is equal to the minVal given
	
	lowerBound, upperBound = findBounds(values, occurences[0], minVal) # bounds for the 0'th occurence of minVal
	currMax = sum(values, lowerBound, upperBound) # currMax holds the maximum weight so far
		
	for x in range(1, len(occurences)): # starting from 1 and going through n-1
		lowerBound, upperBound = findBounds(values, occurences[x], minVal) # finds bounds for x'th occurence
		thisMax = sum(values, lowerBound, upperBound) # calculates sum between calculated bounds
		if (thisMax > currMax):
			currMax = thisMax # replaces maximum possible weight if necessary
	
	print(currMax)