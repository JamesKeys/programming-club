# created by James Keys at Villanova University for Programming Club
# solves Kattis problem found here: kattis.com/alphabetspam

# for counting of whitespace characters
whitespace = '_'
# ASCII representations for lowercase and uppercase letters
lowercase = range(97,123)
uppercase = range(65,91)

# input string to return proportions of
inStr = input()

# number of occurrences of each type
numWhitespace = inStr.count(whitespace)
numLowercase = sum([1 for x in inStr if ord(x) in lowercase])
numUppercase = sum([1 for x in inStr if ord(x) in uppercase])


# proportion of whitespace characters
print(inStr.count(whitespace)/len(inStr))
# proportion of lowercase letters
print(numLowercase/len(inStr))
# proportion of uppercase letters
print(numUppercase/len(inStr))

# all other characters are symbols, print proportion
print((len(inStr)-numWhitespace-numLowercase-numUppercase)/len(inStr))