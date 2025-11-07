# 5014 스타트링크

from collections import deque

INF = 1_000_000

F, S, G, U, D = map(int, input().split())
graph = [INF for _ in range(F+1)]
visited = [False for _ in range(F+1)]
move = [U, -D]

Q = deque()
Q.append(S)
graph[S] = 0
visited[S] = True

while Q:
    now = Q.popleft()

    for i in range(2):
        curr = now + move[i]

        if 1 <= curr <= F and not visited[curr]:
            graph[curr] = min(graph[curr], graph[now]+1)
            visited[curr] = True
            Q.append(curr)

print(graph[G]) if graph[G] != INF else print("use the stairs")