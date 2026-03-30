# 1956 운동

import sys
input = sys.stdin.readline

INF = 1_000_000_000

V, E = map(int, input().split())

dist = [[INF] * (V+1) for _ in range(V+1)]

for i in range(1, V+1):
    dist[i][i] = 0

for _ in range(E):
    a, b, cost = map(int, input().split())
    dist[a][b] = cost

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

answer = INF
for i in range(1, V+1):
    for j in range(1, V+1):
        if dist[i][j] == INF or dist[i][j] == 0: continue
        answer = min(answer, dist[i][j]+dist[j][i])

print(answer if answer != INF else -1)