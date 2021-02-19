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

def transpose(game):
    newGame = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for row in range(4):
        for col in range(4):
            newGame[col][row] = game[row][col]
    return newGame

game = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
game[0] = input().split(' ')
game[1] = input().split(' ')
game[2] = input().split(' ')
game[3] = input().split(' ')

for arr in game:
    for i in range(len(arr)):
        arr[i] = int(arr[i])

direction = int(input())

if direction == 0 or direction == 2:
    slideHorizontal(game, direction-1)
if direction == 1 or direction == 3:
    game = transpose(game)
    slideHorizontal(game, direction-2)
    game = transpose(game)

for arr in game:
    for element in arr:
        print(element, end=' ')
    print()