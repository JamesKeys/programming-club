# Created by James Keys at Villanova University for Programming Club
# Solves Kattis problem found here: https://open.kattis.com/problems/chess

# number of test cases
numCases = int(input())

# convert the alphabetic column to a numeric representation
x_pos_dict = {'A': 0, 'B': 1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}
# hold the alphabetic columns to be converted from numeric to alphabetic
x_vals = 'ABCDEFGH'

def isMovable(pointA_x: int, pointA_y: int, pointB_x:int, pointB_y:int):
	"""
	Determine if the bishop can move diagonally from point A to point B.
	"""
	return abs(pointA_x-pointB_x) == abs(pointA_y-pointB_y)

# for each case,
for i in range(numCases):
	# store teh starting and ending x,y coordinates
	positions = input().split()
	startX, startY, endX, endY = x_pos_dict[positions[0]], int(positions[1]), x_pos_dict[positions[2]], int(positions[3])
	
	# if the starting and ending coordinates are the same, no moves, print start/end
	if startX == endX and startY == endY:
		print('0', x_vals[startX], startY)
	# if the end is within one move of the start, print 1 and the start then end coordinates
	elif isMovable(startX,startY,endX, endY):
		print('1', x_vals[startX], startY, x_vals[endX], endY)
	# otherwise, it is 2 moves
	else:
		# hold a list to store the middle coordinate
		solutionMove = []
		
		# for each possible x, 
		for x in range(8):
			# and each possible y
			for y in range(8):
				# if this coordinate can be reached from the start and can reach the end,
				if isMovable(startX,startY,x,y) and isMovable(x,y,endX,endY):
					# append the coordinates to the list
					solutionMove.append(x_vals[x]+' '+str(y))
		# if a solution was found, print
		if len(solutionMove) > 0:
			print('2', x_vals[startX], startY, solutionMove[0], x_vals[endX], endY)
		# otherwise, it's impossible to move from start to end
		else:
			print('Impossible')