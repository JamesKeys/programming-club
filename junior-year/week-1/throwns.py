numKids, numCommands = input().split()
numKids, numCommands = int(numKids), int(numCommands)
rawCommands = input().split()
commands = []

isUndo = False
for command in rawCommands:

	if(isUndo):
		commands = commands[0:-1*int(command)]
		isUndo = False
	elif (command == 'undo'):
		isUndo = True
	else:
		command = int(command)
		commands.append(command)

print(sum(commands) % numKids)