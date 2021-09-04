# Created by James Keys at Villanova University for Programming Club
# Solves Kattis problem found here: https://open.kattis.com/problems/mathhomework

# inputs given, number of legs for each type of animal b,c,d and total legs l
b,c,d, l = [int(a) for a in input().split()]

# maximum values possible for each type of animal
maxB, maxC, maxD = int(l/b), int(l/c), int(l/d)

# boolean to hold if we need to print 'impossible'
isImpossible = True

# iterate through each possible number of animals from 0 to their max values
for iterB in range(maxB+1):
	for iterC in range(maxC+1):
		for iterD in range(maxD+1):
			
			# if each type of animal*their legs sum together to equal the total
			if iterB*b+iterC*c+iterD*d == l:
				# print the counts of each that work and declare possibility
				print(iterB, iterC, iterD)
				isImpossible = False

# if no solution has been found, print impossible
if isImpossible:
	print('impossible')