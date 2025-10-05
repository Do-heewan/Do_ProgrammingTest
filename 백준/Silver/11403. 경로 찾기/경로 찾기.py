# 11403 경로 찾기

INF = 1_000_000_000

N = int(input())

graph = [[INF] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    lst = list(map(int, input().split()))
    for j in range(1, len(lst)+1):
        if lst[j-1] == 1:
            graph[i][j] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()