# 2170 선 긋기

import sys
input = sys.stdin.readline

N = int(input())
line = [list(map(int, input().split())) for _ in range(N)]
line.sort(key=lambda x : x[0])

tmp = [line[0][0], line[0][1]]
ans = 0
for i in range(1, N):
    x, y = line[i]
    
    if tmp[0] <= x and y <= tmp[1]:
        continue
    elif x < tmp[0] and tmp[1] < y:
        tmp = [x, y]
    elif x <= tmp[0] <= y:
        tmp[0] = x
    elif x <= tmp[1] <= y:
        tmp[1] = y
    else:
        ans += tmp[1] - tmp[0]
        tmp = [x, y]

else:
    if tmp:
        ans += tmp[1] - tmp[0]
print(ans)