# Created by James Keys at Villanova University for Programming Club
# Solves Kattis problem found here: https://open.kattis.com/problems/thisaintyourgrandpascheckerboard


def check_rows(board:list):
	"""
	Checks every row and returns if each row has n/2 white and n/2 black squares.
	
	:param: board (list): board filled with 1's for black and 0's for white
	
	:returns: bool iff every row has equal black and white values
	"""
	for row in board:
		if sum(row) != len(row)/2:
			return False
	return True
def check_three(board:list):
	"""
	Checks to see if any row has 3 of the same colors in a row.
	
	:param: board (list): board filled with 1's for black and 0's for white

	:returns: bool iff every row does not contain 3 colors in a row
	"""
	for row in board:
		for col_i in range(0, len(row)-3):
			if sum(row[col_i:col_i+3]) == 0 or sum(row[col_i:col_i+3]) == 3:
				return False
	return True

# number of squares on the chessboard
num_squares = int(input())

# chessboard being used, with 1's representing black, 0's representing white
board = [[1 if square=='B' else 0 for square in list(input())] for row_i in range(num_squares)]
# transposed chessboard
transp_board = [list(x) for x in list(zip(*board))]

# if it passes all checks, print 1, else print 0
if check_rows(board) and check_rows(transp_board) and check_three(board) and check_three(transp_board):
	print(1)
else:
	print(0)