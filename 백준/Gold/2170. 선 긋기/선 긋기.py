# 2170 선 긋기

import sys
input = sys.stdin.readline

N = int(input())
line = [list(map(int, input().split())) for _ in range(N)]
line.sort(key=lambda x : x[0])

start, end = line[0]
ans = 0

for i in range(1, N):
    x, y = line[i]

    # 그여진 선과 현재 선이 겹치면
    if x <= end:
        end = max(end, y)

    # 안 겹치면
    else:
        ans += end-start
        start, end = line[i]

ans += end-start

print(ans)    