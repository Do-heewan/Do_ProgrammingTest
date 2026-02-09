# 2157 여행

N, M, K = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(K):
    a, b, cost = map(int, input().split())
    if a < b: graph[a].append([b, cost])

dp = [[-1] * (M+1) for _ in range(N+1)]
dp[1][1] = 0

for curr in range(1, N+1):
    for arrived in range(1, M):
        if dp[curr][arrived] == -1:
            continue

        for next, cost in graph[curr]:
            dp[next][arrived+1] = max(dp[next][arrived+1], dp[curr][arrived]+cost)

print(max(dp[N]))