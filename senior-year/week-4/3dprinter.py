num_statues = int(input())

num_machines = 1
num_days = 0

if num_statues != 1:
    num_days += 1

while(num_machines*2 < num_statues):
    num_days += 1
    num_machines *= 2

print(num_days + 1)