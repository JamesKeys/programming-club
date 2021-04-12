# Created by Jim Keys at Villanova University
# Solves Kattis problem found here: https://open.kattis.com/problems/encodedmessage

import math # used for getting square root

numTrials = int(input())

for x in range(numTrials):
    code = [] # this will store the input in a two dimensional array, allowing for transposing
    preCodeMessage = input()
    numSquares = int(math.sqrt(len(preCodeMessage))) # this is both the number of columns and rows since
						     # it is a square
    for i in range(numSquares):
        code.append([]) # adds a row each time
        for r in range(numSquares-1, -1, -1): # in reverse to fix for appending
            code[i].append(preCodeMessage[i*numSquares+r]) # add the n'th letter to the code square
            
    for i1 in range(numSquares):
        for i2 in range(numSquares):
            print(code[i2][i1], end='') # loops through column-major order to get decoded message, printing each character
    print() # print newline