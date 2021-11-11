# Created by James Keys at Villanova University for programming club
# Solves Kattis problem found here: https://open.kattis.com/problems/proofs

# dictionary to hold variables which have been instantiated, faster than list implementation
seen_variables = {}

# number of lines to scan through
num_lines = int(input())

# by creating a function, the return value can cut the run-time short if needed
def ans():
	# for each line index,
	for line_i in range(num_lines):
		# split the line on spaces
		this_line = input().split()
		
		# if the line is a declaration, add to dictionary with value 1
		if this_line[0] == "->":
			seen_variables[this_line[1]] = 1
		# else, loop through the values used in the creation of a new variable
		else:
			for str_i in range(len(this_line)):
				# if we've reached the end, add the new variable
				if this_line[str_i] == "->":
					seen_variables[this_line[str_i+1]] = 1
				# else, check to see if we've seen this variable before, if not, return the line+1
				else:
					if this_line[str_i] not in seen_variables:
						return line_i+1
	return 0
	
ret_val = ans()
if ret_val:
	print(ret_val)
else:
	print('correct')