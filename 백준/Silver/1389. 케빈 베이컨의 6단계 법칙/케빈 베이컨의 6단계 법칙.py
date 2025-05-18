# 1389 케빈 베이컨의 6단계 법칙

from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(num):
    visited = [False for _ in range(N+1)]
    result = []

    visited[num] = True

    Q = deque()
    Q.append([num, 0])
    result.append([num, 0])
    
    while Q:
        c, b_num = Q.popleft()

        b_num += 1
        for ix in graph[c]:
            if not visited[ix]:
                Q.append([ix, b_num])
                result.append([ix, b_num])
                visited[ix] = True

    return result
    
bacon_num = []
for i in range(1, N+1):
    bfs_result = bfs(i)
    val = 0

    for j in range(len(bfs_result)):
        val += bfs_result[j][1]
    
    bacon_num.append(val)

print(bacon_num.index(min(bacon_num)) + 1)