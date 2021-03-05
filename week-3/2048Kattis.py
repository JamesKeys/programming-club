# Created by Jim Keys at Villanova University
# Solves Kattis Problem found here: https://open.kattis.com/problems/2048

def slideLeft(arr):
    # Starts from the right, sliding the integer to the left
    # iff the space to the left of it is open (0)
    for x in range(3):
            for i in range(3,0,-1):
                if (arr[i-1] == 0):
                    arr[i-1] = arr[i]
                    arr[i] = 0
def addLeft(arr):
    # Starts from the left, adding the integer to the right
    # iff the integer to the right matches, replaces with 0
    for i in range(3):
        if (arr[i] == arr[i+1]):
            arr[i] = arr[i] + arr[i+1]
            arr[i+1] = 0

def slideRight(arr):
    # Starts from the left, sliding the integer to the right
    # iff the space to the right of it is open (0)
    for x in range(3):
            for i in range(3):
                if (arr[i+1] == 0):
                    arr[i+1] = arr[i]
                    arr[i] = 0
def addRight(arr):
    # Starts from the right, adding the integer to the left
    # iff the integer to the left matches, replaces with 0
    for i in range(3,0,-1):
        if (arr[i] == arr[i-1]):
            arr[i] = arr[i] + arr[i-1]
            arr[i-1] = 0

def slideHorizontal(game, leftRight):
    # Slides the tiles in the board and adds matching numbers
    # leftRight = -1 for a LEFT shift, else for a RIGHT shift
    for arr in game:
        if (leftRight == -1):
            slideLeft(arr)
            addLeft(arr)
            slideLeft(arr)
        else:
            slideRight(arr)
            addRight(arr)
            slideRight(arr)

def transpose(game):
    # Had to create because Kattis doesn't allow for NumPy
    newGame = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for row in range(4):
        for col in range(4):
            newGame[col][row] = game[row][col]
    return newGame

# Had to implement with 0's because Kattis doesn't allow numpy.zeros
game = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

game[0] = input().split(' ')
game[1] = input().split(' ')
game[2] = input().split(' ')
game[3] = input().split(' ')

# Had to implement element-wise casting because Kattis doesn't allow numpy.astype
for arr in game:
    for i in range(len(arr)):
        arr[i] = int(arr[i])

# LEFT: direction = 0
# UP: direction = 1
# RIGHT: direction = 2
# DOWN: direction = 3
direction = int(input())

if (direction == 0 or direction == 2):
    slideHorizontal(game, direction-1)
if (direction == 1 or direction == 3):
    game = transpose(game) # Transposing the board allows me to use the function I previously created
    slideHorizontal(game, direction-2)
    game = transpose(game) # And transpose back to reorient the board correctly

for arr in game:
    for element in arr:
        print(element, end=' ')
    print()
