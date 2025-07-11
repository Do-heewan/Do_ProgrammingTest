# 2096 내려가기

N = int(input())

dp_min = [0, 0, 0]
dp_max = [0, 0, 0]

for i in range(N):
    lst = list(map(int, input().split()))
    dp_max = [lst[0] + max(dp_max[:2]), lst[1] + max(dp_max), lst[2] + max(dp_max[1:])]
    dp_min = [lst[0] + min(dp_min[:2]), lst[1] + min(dp_min), lst[2] + min(dp_min[1:])]

print(max(dp_max), min(dp_min))