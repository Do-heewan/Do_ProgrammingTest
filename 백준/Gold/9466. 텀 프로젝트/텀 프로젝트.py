# 9466 텀 프로젝트

import sys
sys.setrecursionlimit(111111) #충분한 재귀 깊이를 주어 오류를 예방

T = int(input())

def dfs(num):
    global result

    visited[num] = True
    target = graph[num]
    cycle.append(num)

    if visited[target]:
        if target in cycle:
            result += cycle[cycle.index(target):]
        return
    
    else:
        dfs(target)

for _ in range(T):
    N = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [False] * (N+1)
    result = []

    for i in range(1, N+1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(N - len(result))
