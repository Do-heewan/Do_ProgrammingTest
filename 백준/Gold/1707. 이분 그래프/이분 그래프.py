# 1707 이분 그래프

import sys
input = sys.stdin.readline

from collections import deque

def bfs(n):
    Q = deque()
    Q.append(n)
    visited[n] = 1

    while Q:
        curr = Q.popleft()

        for ix in graph[curr]:
            if visited[ix] == 0:
                visited[ix] = (-1) * visited[curr]
                Q.append(ix)
            elif visited[ix] == visited[curr]:
                return False
            
    return True

T = int(input())

for _ in range(T):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [0] * (V+1)

    isAble = True
    for i in range(1, V+1):
        if visited[i] == 0:
            if not bfs(i):
                isAble = False
                break
    
    print("YES" if isAble else "NO")