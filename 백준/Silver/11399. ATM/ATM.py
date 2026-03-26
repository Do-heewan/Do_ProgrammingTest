# 11399 ATM

N = int(input())
times = list(map(int, input().split()))
times.sort()

prefix_sum = [0]
for i in range(N):
    prefix_sum.append(times[i]+prefix_sum[i])

print(sum(prefix_sum))