import numpy as np

def slideHorizontal(game, leftRight):
	# -1 means left, 1 means right
	for arr in game:
		if leftRight == -1:
			slideLeft(arr)
			addLeft(arr)
			slideLeft(arr)
		else:
			slideRight(arr)
			addRight(arr)
			slideRight(arr)

def slideLeft(arr):
	for x in range(3):
			for i in range(3,0,-1):
				if arr[i-1] == 0:
					arr[i-1] = arr[i]
					arr[i] = 0
def addLeft(arr):
	for i in range(3):
		if arr[i] == arr[i+1]:
			arr[i] = arr[i] + arr[i+1]
			arr[i+1] = 0

def slideRight(arr):
	for x in range(3):
			for i in range(3):
				if arr[i+1] == 0:
					arr[i+1] = arr[i]
					arr[i] = 0
def addRight(arr):
	for i in range(3,0,-1):
		if arr[i] == arr[i-1]:
			arr[i] = arr[i] + arr[i-1]
			arr[i-1] = 0

game = np.zeros([4,4])
game[0] = input().split()
game[1] = input().split()
game[2] = input().split()
game[3] = input().split()

game = game.astype(int)

direction = int(input())

if direction == 0 or direction == 2:
	slideHorizontal(game, direction-1)
if direction == 1 or direction == 3:
	game = np.transpose(game)
	slideHorizontal(game, direction-2)
	game = np.transpose(game)

for arr in game:
	for element in arr:
		print(element, end=' ')
	print()