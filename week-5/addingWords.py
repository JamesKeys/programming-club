# Created by Jim Keys at Villanova University
# Solves Kattis problem found here: https://open.kattis.com/problems/addingwords

masterDict = {} # this holds the associations between the String word and the int value

def removeKeyWithValue(value): # This will remove the key value pair which contains value
				# used when a new string takes an old integer value
	for key in masterDict.keys():
		if masterDict[key] == value:
			del masterDict[key]
def defineStatement(inList): # This is used to enter a new string/int pairing
	if inList[1] in masterDict.values(): # if the integer value is already in the dict
		removeKeyWithValue(inList[1]) # remove the key value associated with the value
	masterDict[inList[0]] = int(inList[1]) # create new key value pair
def findKey(value): # used to find the key associated with the integer value
	for key in masterDict.keys():
		if masterDict[key] == value:
			return key
	return 'noKey' # returns noKey if there is no key associated with integer value
def calcStatement(inList): # used to calculate the equation
	sum = 0 # running sum
	for i in range(0, len(inList), 2):
		if inList[i] not in masterDict: # exit if any value is unaccounted for
			return 'unknown'
		else:
			if i == 0: # always will be "added" to sum
				sum = masterDict[inList[i]]
			elif inList[i-1] == '+':
				sum += masterDict[inList[i]]
			elif inList[i-1] == '-':
				sum -= masterDict[inList[i]]
	if findKey(sum) == 'noKey':
		return 'unknown' # don't have a key value for the end value
	else:
		return findKey(sum)
	
while(True): # keep getting inputs
	try:
		inStr = input().split() # stores as ['calc', 'foo', '+', 'bar', '=']
		
		if inStr[0] == 'def': # define statement starting at i = 1
			defineStatement(inStr[1:])
		elif inStr[0] == 'calc': # calculate statement starting at i = 1
			printVal = calcStatement(inStr[1:])
			for i in range(1, len(inStr), 1):
				print(inStr[i], end=' ') # print all values given with spaces
			print(printVal) # print sum value
		elif inStr[0] == 'clear': # clear all associations
			masterDict = {}
	except Exception as e: # triggered with EOF
		break