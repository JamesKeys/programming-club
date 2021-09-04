# Created by James Keys at Villanova University for Programming Club
# Solves Kattis problem found here: https://open.kattis.com/problems/perket

def prod(l: list):
	"""
	calculates and returns the product of a list.
	"""
	retVal = 1
	for item in l:
		retVal = retVal * item
	return retVal

def generatePowerSet(l: list):
	"""
	Create and return all possible ingredient combinations.
	"""
	retList = []
	
	# Use bitmasking to incrementally generate all possible combinations
	for counter in range(2**len(l)):
		
		# Add new combination
		retList.append([])
		
		# Check the j'th bit to see if it is "on"
		for j in range(len(l)):
			if(counter & (1 << j)) != 0:
				# if it is, append j (representing the index)
				retList[counter].append(j)
	# return all except the empty set
	return retList[1:]

def getIndices(ing: list, indices: list):
	"""
	Return the values at positions indices.
	"""
	retVal = []
	for index in indices:
		retVal.append(ing[index])
	return retVal
	
# number of ingredients to choose from
numIngredients = int(input())

sourness = [] # total sourness is the product of all individual ingredients
bitterness = [] # total bitterness is the sum of all individual ingredients

# store the values of all the ingredients
for ingredientI in range(numIngredients):
	taste = [int(x) for x in input().split()]
	sourness.append(taste[0])
	bitterness.append(taste[1])
	
# generate all of the possible ingredient combinations
possibleIngredients = generatePowerSet(sourness)

# create list to store the possible sum/product values
possibleFlavors = []

# for each unique ingredient combination,
for thisCombo in possibleIngredients:
	# generate the product of the ingredients (sourness) located at the indices of this combination
	sour = prod(getIndices(sourness, thisCombo))
	# generate the sum of the ingredients (bitterness) located at the indices of this combination
	bitter = sum(getIndices(bitterness, thisCombo))
	# calculate and append the difference between the sourness and bitterness
	possibleFlavors.append(abs(bitter-sour))

# print the minimum difference found in possible ingredients between sourness and bitterness
print(min(possibleFlavors))