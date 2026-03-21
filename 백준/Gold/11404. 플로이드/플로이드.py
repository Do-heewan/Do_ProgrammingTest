# 11404 플로이드

INF = 1_000_000_000

N = int(input())
M = int(input())

dist = [[INF] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a, b, cost = map(int, input().split())
    dist[a][b] = min(dist[a][b], cost)

for i in range(1, N+1):
    dist[i][i] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if dist[i][k] != INF and dist[k][j] != INF:
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

for d in dist[1:]:
    for i in d[1:]:
        if i == INF:
            print(0, end=' ')
            continue
        print(i, end=' ')
    print()