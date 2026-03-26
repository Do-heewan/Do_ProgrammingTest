# 1931 회의실 배정

import sys
input = sys.stdin.readline

N = int(input())

times = []
for _ in range(N):
    start, end = map(int, input().split())
    times.append([start, end])

times.sort(key=lambda x : (x[1], x[0]))

wait = 0
cnt = 0
for start, end in times:
    if start == end:
        cnt += 1
        wait = end

    elif start >= wait:
        cnt += 1
        wait = end

print(cnt)