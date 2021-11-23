# Created by James Keys at Villanova University for Programming Club
# Solves Kattis problem found here: https://open.kattis.com/problems/erase

# number of times they want to switch data back and forth
num_switch = int(input())

# store the initial and end states
initial = [int(bit) for bit in list(input())]
end = [int(bit) for bit in list(input())]

# if it's odd, we need to flip every bit
if num_switch % 2 == 1:
	initial = [1 if bit==0 else 0 for bit in initial]

# if they're equal, each bit has been flipped appropriately
if initial == end:
	print('Deletion succeeded')
else:
	print('Deletion failed')