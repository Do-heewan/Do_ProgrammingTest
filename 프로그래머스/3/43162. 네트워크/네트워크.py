from collections import deque

def solution(n, computers):
    def bfs(n):
        if visited[n]:
            return 0
        
        Q = deque()
        Q.append(n)
        visited[n] = True
        
        while Q:
            c = Q.popleft()
            
            for ix in graph[c]:
                if not visited[ix]:
                    Q.append(ix)
                    visited[ix] = True
                    
        return 1
    
    cnt = len(computers)
    graph = [[] for _ in range(cnt)]
    
    for i in range(cnt):
        for j in range(cnt):
            if i == j:
                continue
            
            elif computers[i][j] == 1:
                graph[i].append(j)
    
    visited = [False] * cnt
    
    ans = 0
    for i in range(cnt):
        ans += bfs(i)
    
    return ans