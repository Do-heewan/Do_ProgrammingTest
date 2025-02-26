# 15654 N과 M (5)

import sys
from itertools import permutations

N, M = map(int, input().split())
li = list(map(int, input().split()))
li.sort()

comb = list(permutations(li, M))

for ix in comb:
    print(*ix)