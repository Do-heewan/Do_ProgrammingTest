# 19538 루머

import sys
from collections import deque
input = sys.stdin.readline

def bfs(lst: list):
    Q = deque()

    for ix in lst:
        Q.append(ix)
        visited[ix] = True
        time[ix] = 0

    for i in range(1, N+1):
        roumer[i] = (len(graph[i])+1) // 2

    while Q:
        c = Q.popleft()

        for ix in graph[c]:
            roumer[ix] -= 1
            if not visited[ix] and roumer[ix] <= 0:
                Q.append(ix)
                visited[ix] = True
                time[ix] = time[c] + 1

N = int(input())

graph = [[0]] 
for _ in range(N):
    rel = list(map(int, input().split()))
    graph.append(rel[:len(rel)-1])

M = int(input())

first = list(map(int, input().split()))

visited = [False] * (N+1)
time = [-1] * (N+1)
roumer = [0] * (N+1)

bfs(first)

print(*time[1:])