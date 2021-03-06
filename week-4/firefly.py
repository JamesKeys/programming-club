# Created by Jim Keys at Villanova University
# Solves Kattis problem found here: https://open.kattis.com/problems/firefly

length, height = input().split() # Length is how many stalagmites/stalactites in cave
length, height = int(length), int(height) # Height is the height of the cave

barriers = [0 for a in range(height)]
below = [0 for a in range(height)] # the a'th value holds the number of stalagmites of height a
above = [0 for a in range(height)] # the a'th value holds the number of stalactites of length a
	
for x in range(length):
	iHeight = int(input()) # This is the height of the stalagmite if even, stalactite if odd
	if(x%2 == 0):
		below[iHeight-1] += 1
	else:
		above[height-iHeight] += 1

barriers[height-1] = below[height-1] # Initialize the highest value, there is no summation done

for level in range(height-2, -1, -1):
	below[level] += below[level+1] # Sum the value above into the current, since it's cumulative
	barriers[level] = below[level] # This updated value contains all above the current level

barriers[0] += above[0] # Incrementing here to preserve previous effort, no summation done

for level in range(1,height):
	above[level] += above[level-1] # Same as before, sum the value below into current
	barriers[level] += above[level] # Updated value contains all below the current

minVal = min(barriers)
print(minVal, barriers.count(minVal))