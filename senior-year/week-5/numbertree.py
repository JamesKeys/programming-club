# Created by James Keys at Villanova University for Programming Club
# Solves Kattis problem found here: https://open.kattis.com/problems/numbertree

height = input()

# if the only input is the height of the tree, print root
if len(height.split()) == 1:
	print((2**(int(height)+1))-1)
# else, there is a space, with the height and the path
else:
	# path is the directions, ex. "LRLL"
	path = height.split()[1]
	
	# height of the tree
	height = int(height.split()[0])+1
	
	# number of turns to take
	depth = len(path)
	
	# root node value
	root = 2**height-1

	# once we find the starting level, this decrements to the right value
	offset = 0
	for turn_i in range(0,len(path)):
		if path[turn_i] == 'R':
			offset += 2**(depth-turn_i-1)

	# calculate the desired node's value	
	end = root-(2**depth-1)-offset
	print(end)