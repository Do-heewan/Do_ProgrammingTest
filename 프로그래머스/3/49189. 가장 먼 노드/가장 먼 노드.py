from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for e in edge:
        start, end = e[0], e[1]
        graph[start].append(end)
        graph[end].append(start)
        
    visited = [-1] * (n+1)
    
    Q = deque()
    Q.append(1)
    visited[1] = 0
    
    while Q:
        curr = Q.popleft()
        
        for ix in graph[curr]:
            if visited[ix] == -1:
                visited[ix] = visited[curr] + 1
                Q.append(ix)
    
    max_distance = max(visited)
    ans = visited.count(max_distance)
    
    return ans