# Created by James Keys at Villanova University for Programming Club
# Solves Kattis problem found here: https://open.kattis.com/problems/owlandfox

# number of cases to go through
num_cases = int(input())

for case_i in range(num_cases):
	
	# string representation of input number
	in_num = input()
	
	# integer containing current number
	start_num = int(in_num)
	
	# sum of individual numbers from starting number
	target_num = sum([int(x) for x in list(in_num)])
	
	# while sum of individual numbers from current number doesn't equal target-1, decrement
	while sum([int(x) for x in list(str(start_num))]) != target_num-1:
		start_num -= 1
	
	print(start_num)