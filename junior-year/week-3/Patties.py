# Created by Jim Keys at Villanova University
# Solves problem on Kattis found here: https://open.kattis.com/problems/flippingpatties

import math

numBurgers = int(input()) # Number of inputs coming

timeInteractions = [] # Stores all the times there is an action taking place

for x in range(numBurgers):
	timeToCook, timeFinish = input().split(' ') # Splits the cook time from the desired finish time
	timeInteractions.append(int(timeFinish)) # Timestamp the cook needs to take the patty off the grill
	timeInteractions.append(int(timeFinish)-int(timeToCook)) # Timestamp the cook needs to flip the patty at
	timeInteractions.append(int(timeFinish)-int(timeToCook)*2) # Timestamp the cook needs to put the patty on at

overloadedTime = max(timeInteractions, key = timeInteractions.count) # Finds the busiest timestamp
numActions = timeInteractions.count(overloadedTime) # Counts the number of actions at that timestamp

print(math.ceil(numActions / 2)) # Every cook has two hands so divide by two, take the ceiling