num_iter = int(input())

ans = 2
for iter_i in range(num_iter):
	ans += ans-1

print(ans**2)