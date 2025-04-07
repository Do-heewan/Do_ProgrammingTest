# 1967 트리의 지름

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N = int(input())

graph = [[] for _ in range(N+1)] # 트리 초기화

for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

# 방문(길이) 표시
visited = [-1 for _ in range(N+1)]
visited[1] = 0 # 루트 노드에선 길이 0

# DFS 탐색
def dfs(num, length):
    for a, b in graph[num]:
        if (visited[a] == -1):
            visited[a] = b + length # 현재의 길이와 하위 노드로 갈 때의 길이 합을 저장
            dfs(a, visited[a])

# 루트에서부터 모든 노드까지의 거리 탐색
dfs(1, 0)

start = visited.index(max(visited)) # 루트에서 부터 가장 멀리 떨어진 노드

visited = [-1 for _ in range(N+1)] # 방문 초기화
visited[start] = 0

dfs(start, 0) # start로부터 모든 노드까지의 거리 탐색

print(max(visited)) # 가장 긴 길이가 트리의 지름이 된다.