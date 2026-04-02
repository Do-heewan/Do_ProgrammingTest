# 2631 줄세우기

N = int(input())
lst = [int(input()) for _ in range(N)]

lis = [1] * N
for i in range(N):
    for j in range(i):
        if lst[i] > lst[j]:
            lis[i] = max(lis[i], lis[j]+1)

print(N-max(lis))