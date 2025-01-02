# 2606 바이러스 (BFS)

from collections import deque

n = int(input()) # 노드 갯수(컴퓨터)
v = int(input()) # 엣지 갯수(연결 선)

graph = [[] for i in range(n+1)] # 그래프 초기화
visited = [0] * (n+1) # 방문한 컴퓨터인지 표시

for i in range(v):
    a, b = map(int, input().split())
    graph[a] += [b] # a에 b 연결
    graph[b] += [a] # b에 a 연결 -> 양방향

visited[1] = 1 # 1번부터 시작이기에 1번 표시
Q = deque([1])
while Q:
    c = Q.popleft()
    
    for nx in graph[c]:
        if (visited[nx] == 0):
            Q.append(nx)
            visited[nx] = 1

print(sum(visited) - 1)