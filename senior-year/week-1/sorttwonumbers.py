# Created by James Keys at Villanova University for Programming Club
# Solves Kattis problem found here: https://open.kattis.com/problems/sorttwonumbers

# Read both numbers and split into strings
twonums = [int(a) for a in input().split()]

# Print out the minimum of the two, and then the maximum
print(min(twonums), max(twonums))