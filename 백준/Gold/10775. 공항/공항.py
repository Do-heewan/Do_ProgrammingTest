# 10775 공항

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 8)

def find_root(x):
    if x == parent[x]: return x
    parent[x] = find_root(parent[x])
    return parent[x]

G = int(input())
P = int(input())

plane = [int(input()) for _ in range(P)]

parent = [i for i in range(G+1)]

ans = 0
for p in plane:
    root = find_root(p)

    if root == 0: break

    parent[root] = find_root(root-1)
    ans += 1

print(ans)