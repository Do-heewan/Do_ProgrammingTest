# 2533 사회망 서비스 (SNS)

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 8)

def dfs(n):
    visited[n] = True

    for ix in graph[n]:
        if not visited[ix]:
            dfs(ix)
            dp[n][0] += dp[ix][1]
            dp[n][1] += min(dp[ix][0], dp[ix][1])
            
N = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
dp = [[0, 1] for _ in range(N+1)]

dfs(1)
print(min(dp[1]))