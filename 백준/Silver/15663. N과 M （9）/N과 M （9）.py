from itertools import permutations

N, M = map(int, input().split())

li = list(map(int, input().split()))
li.sort()

perm = set(permutations(li, M))

for ix in sorted(perm):
    print(*ix)