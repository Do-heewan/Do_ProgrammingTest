# 34200 장애물

from collections import deque

INF = 1_000_000

N = int(input())
wall = list(map(int, input().split()))

max_height = max(wall)
way = [INF for _ in range(max_height+2)]
for w in wall:
    way[w] = -1

Q = deque()
Q.append(0)
way[0] = 0
while Q:
    c = Q.popleft()

    for i in [c+1, c+2]:
        if i >= len(way):
            continue

        if i <= max(wall)+1 and way[i] != -1 and way[i] == INF:
            way[i] = min(way[c] + 1, way[i])
            Q.append(i)

print(way[max_height+1] if way[max_height+1] != INF else -1)