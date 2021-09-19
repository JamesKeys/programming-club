# created by James Keys at Villanova University for Programming Club
# solves Kattis problem foudn here: kattis.com/problems/parking2

# number of test cases to go through
numTestCases = int(input())

# for each test case,
for testCaseX in range(numTestCases):

	# the number of stores to visit
	numStores = int(input())
	
	# read in the locations of the stores on the 1-99 integer number line
	storeLocations = [int(x) for x in input().split()]

	# optimal shopping path starts at min, ends at max
	# optimal parking is somewhere between min and max, so double total range
	print(2*(max(storeLocations)-min(storeLocations)))