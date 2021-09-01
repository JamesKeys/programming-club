trials = int(input())

for trial in range(trials):
	moduloK = int(input()) # Value to modulo each fibonnaci number by
	history = [2] # Starting at i = 2
	a, b = 1, 2  # a and b are used to calculate the next number
	while(True):
		temp = b 
		b = b+a # New fibonnaci number
		a = temp # Move a up an index
		history.append(b % moduloK) # Add to list to track what numbers we've seen
		if(history.count(b % moduloK) > 1): # If we've repeated, break the while loop
			break
	
	# Go back and find the index of the first occurrence of the repeated number
	for x in range(len(history)):
		if(history[x] == (b % moduloK)):
			print(x+2) # The person starts at n = 2 so this makes up for that offset
			break