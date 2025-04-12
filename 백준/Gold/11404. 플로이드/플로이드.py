# 11404 플로이드

INF = 1_000_000_000

N = int(input())
M = int(input())

graph = [[INF for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = min(c, graph[a][b])

for a in range(1, N+1):
    for b in range(1, N+1):
        if (a == b):
            graph[a][b] = 0

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, N+1):
    for b in range(1, N+1):
        if (graph[a][b] == INF):
            print(0, end = " ")

        else:
            print(graph[a][b], end = " ")

    print()