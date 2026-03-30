# 11780 플로이드 2

import sys
input = sys.stdin.readline

def get_path(i, j):
    if route[i][j] == -1: return []

    path = [i]
    while i != j:
        i = route[i][j]
        path.append(i)
    
    return path

INF = 1_000_000_000

N = int(input())
M = int(input())

dist = [[INF] * (N+1) for _ in range(N+1)]
route = [[-1] * (N+1) for _ in range(N+1)] # 경로 저장

for i in range(1, N+1):
    dist[i][i] = 0

for _ in range(M):
    a, b, cost = map(int, input().split())
    dist[a][b] = min(dist[a][b], cost)
    route[a][b] = b

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k]+dist[k][j]
                route[i][j] = route[i][k] # 경로 갱신

# N개의 줄 출력 : 플로이드-워셜 결과
for i in range(1, N+1):
    for j in range(1, N+1):
        if dist[i][j] == INF: 
            print(0, end=' ')
            continue
        print(dist[i][j], end=' ')
    print()

# NxN개의 줄 출력 : 각 점에서 다음 점으로 가는 경로 출력
for i in range(1, N+1):
    for j in range(1, N+1):
        path = get_path(i, j)
        print(len(path), *path)