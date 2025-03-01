# 15663 N과 M (9)

import sys
from itertools import permutations

input = sys.stdin.readline

N, M = map(int, input().split())

li = list(map(int, input().split()))
li.sort()

perm = set(permutations(li, M))

for ix in sorted(perm): # set을 취하는 과정에서 정렬이 풀릴 수 있기 때문에 다시 한 번 정렬
    print(*ix)