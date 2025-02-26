# 15650 N과 M (2)

import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

li = []
for i in range(1, N+1):
    li.append(i)

comb = list(combinations(li, M))

for ix in comb:
    print(*ix)