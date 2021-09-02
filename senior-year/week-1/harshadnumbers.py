# Created by James Keys at Villanova University for Programming Club
# Solves Kattis problem found here: https://open.kattis.com/problems/harshadnumbers

# read in the number given
inNum = int(input())

def isHarshad(x: int):
	""" Method that detects if x is a harshad number, returning True or False """	
	
	# calculate the sum of each digit in the number
	sumNum = sum([int(a) for a in str(x)])
	
	# return if the original number is divisible by the sum of the digits
	return (x/sumNum) % 1 == 0

# loop until we have found a harshad number
while not isHarshad(inNum):
	inNum += 1

# print the first found harshad number
print(inNum)