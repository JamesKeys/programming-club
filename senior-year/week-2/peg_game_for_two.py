#        0
#       1  2
#      3  4  5
#    6  7  8  9
#  10 11 12 13 14

neighbors = {
	0 : [[1,3],[2,5]],
	1 : [[3,6],[4,8]],
	2 : [[4,7],[5,9]],
	3 : [[1,0],[4,5],[6,10],[7,12]],
	4 : [[7,11],[8,13]],
	5 : [[2,0],[4,3],[8,12],[9,14]],
	6 : [[3,1],[7,8]],
	7 : [[4,2],[8,9]],
	8 : [[4,1],[7,6]],
	9 : [[5,2],[8,7]],
	10 : [[6,3],[11,12]],
	11 : [[7,4],[12,13]],
	12 : [[11,10],[7,3],[8,5],[13,14]],
	13 : [[12,11],[8,4]],
	14 : [[13,12],[9,5]]
}

def hasMove(board):
	for i in range(15):
		for neighbor in neighbors[i]:
			if board[neighbor[0]] == 0:
				return True
	return False
def findBestI(board):
	best_score = 0
	new_board = 
	for i in range(15):
		for neighbor in neighbors[i]:
			if board[neighbor[0]] == 0 and board[neighbor[0]]*board[neighbor[1]] > best_score:
				best_score = board[neighbor[0]]*board[neighbor[1]]
				

board = []
jacquez_score, alia_score = 0,0
for i in range(5):
	row = input().split()
	for item in row:
		board.append(int(item))

while hasMove(board):
	
print(hasMove(board))\