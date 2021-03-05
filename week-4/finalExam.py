# Created by Jim Keys at Villanova University
# Solves Kattis problem found at https://open.kattis.com/problems/finalexam2

numQuestions = int(input())

lastQuestion = "" # This stores the answer to the previous question
score = 0 # This is the current number of correct answers

for q in range(numQuestions):
	qAns = input()
	if (qAns == lastQuestion): # If the n'th answer == n-1'th answer, he still got it right
		score += 1
	else:
		lastQuestion = qAns # Reset previous question's answer 
		
print(score)