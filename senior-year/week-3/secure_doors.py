building = []

log_len = int(input())
for line_i in range(log_len):
	action, person = input().split()
	
	if action == 'entry':
		if person in building:
			print(person, 'entered (ANOMALY)')
		else:
			print(person, 'entered')
			building.append(person)
	elif action == 'exit':
		if person in building:
			print(person, 'exited')
			building.remove(person)
		else:
			print(person, 'exited (ANOMALY)')