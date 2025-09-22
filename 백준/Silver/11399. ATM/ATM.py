# 11399 ATM

N = int(input())
time = list(map(int, input().split()))
time.sort()

curr = 0
total = 0

for t in time:
    curr += t
    total += curr

print(total)