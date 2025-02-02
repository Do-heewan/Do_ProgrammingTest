# 7568 덩치

import sys
input = sys.stdin.readline

N = int(input())

li = []
for _ in range(N):
    weight, height = map(int, input().split())
    li.append([weight, height])

for ix in li:
    rank = 1
    for jx in li:
        if (ix[0] < jx[0]) and (ix[1] < jx[1]):
            rank += 1

    print(rank, end = " ")