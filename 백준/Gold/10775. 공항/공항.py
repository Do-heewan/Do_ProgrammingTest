# 10775 공항

import sys
input = sys.stdin.readline

def find_root(x):
    if x == parent[x]: return parent[x]
    parent[x] = find_root(parent[x])
    return parent[x]

G = int(input())
P = int(input())

parent = [i for i in range(G+1)]

ans = 0
for _ in range(P):
    g = int(input())

    root = find_root(g)

    if root == 0:
        break

    parent[root] = find_root(root-1)
    ans += 1

print(ans)