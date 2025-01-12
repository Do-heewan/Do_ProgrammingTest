# 2605 줄 세우기

N = int(input())
num = list(map(int, input().split()))

li = []
for i in range(1, N+1):
    if (num[i-1] == 0):
        li.append(i)
    else:
        li.insert(len(li) - num[i-1], i)

print(*li)