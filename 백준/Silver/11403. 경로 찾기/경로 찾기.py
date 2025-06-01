# 11403 경로 찾기

N = int(input())

INF = 1_000_000_000

graph = [[INF for _ in range(N+1)] for _ in range(N+1)]
for i in range(1, N+1):
    lst = list(map(int, input().split()))
    for j in range(len(lst)):
        if (lst[j] == 1):
            graph[i][j+1] = 1

# 플로이드-워셜 점화식
for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, N+1):
    for b in range(1, N+1):
        if (graph[a][b] == INF):
            print(0, end = " ")
        else:
            print(1, end = " ")
    print()