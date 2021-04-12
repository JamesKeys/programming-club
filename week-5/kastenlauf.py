# Created by Jim Keys at Villanova University
# Solves Kattis problem found here: https://open.kattis.com/problems/kastenlauf

numCases = int(input())

def calcDistance(x1, y1, x2, y2):
	# IN: int x1, y1 coordinates of first store, int x2, y2 coordinates of second store
	# OUT: int Manhattan distance between the two stores, difference of x's + difference of y's
	return abs(x2-x1)+abs(y2-y1)
def getLength(paths):
	# Used to determine if any new stops have been added, loops through 2d list to
	# Check if the total number of stops has increased, meaning it may not be done
	retVal = 0
	for list in paths:
		for item in list:
			retVal += 1
	return retVal
def createStop(paths, iToWorkOn):
	# IN: 2d list paths holding the stores within 1000m of the i'th store
	# int iToWorkOn holding the index to update, adding all stores within 1000m of
	# all the stores within 1000m of the iToWorkOn store
	
	# Go through each store within reach
	for store in paths[iToWorkOn]:
		
		# Go through each store within reach of that one
		for nextStore in paths[store]: 
			
			# If it wasn't originally in reach, and isn't the current store
			if nextStore not in paths[iToWorkOn] and nextStore != iToWorkOn:
				# add to reachability for the iToWorkOn's store
				paths[iToWorkOn].append(nextStore) 

	return paths # Return updated list, with the index iToWorkOn updated

for case in range(numCases):
	
	# Increased by two to account for starting location and final location
	numStores = int(input()) + 2
	
	stores = [] # The i'th index holds the [x,y] coordinates of the i'th store
	paths = [] # The i'th index holds the i'th store's available neighbors to travel to
	
	for store in range(numStores):
		xy = input().split() # Turn "1000 1000" into ["1000", "1000"]
		stores.append([int(xy[0]), int(xy[1])]) # Turn ["1000", "1000"] into [[1000, 1000], ..., ...]
	
	# Loop through all stores to add their initial neighbors
	for currStore in range(numStores):
		paths.append([])
		for nextStore in range(numStores):
			distance = calcDistance(stores[currStore][0], stores[currStore][1], stores[nextStore][0], stores[nextStore][1])
			if distance > 0 and distance <= 50*20: # Checks to make sure it isn't itself, and within reach
				paths[currStore].append(nextStore)
	
	origLength = getLength(paths) # Pre-update
	newLength = -1 # Post-update
	
	while(origLength != newLength): # If there was an update to the neighbor list, re-update
		origLength = getLength(paths)

		for store in range(len(paths)):
			createStop(paths, store) # Get neighbor of neighbor and assign to self's neighbors

		newLength = getLength(paths)
	
	if (numStores-1) in paths[0]:
		print('happy') # If the initial location (start) has the final location (goal) as a neighbor, happy
	else:
		print('sad') # If the final location is not a neighbor of the initial location, sad