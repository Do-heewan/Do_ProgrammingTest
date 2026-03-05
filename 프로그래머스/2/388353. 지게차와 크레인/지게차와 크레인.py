from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y, carrier, visited, stor, N, M): 
    Q = deque()
    Q.append([x, y])
    visited[x][y] = True
    
    while Q:
        cx, cy = Q.popleft()
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if 0 <= nx < (N+2) and 0 <= ny < (M+2) and not visited[nx][ny]:
                # 한 자리면 공기와 닿는 것들 제거
                if len(carrier) == 1:
                    if stor[nx][ny] == 0:
                        Q.append([nx, ny])
                        visited[nx][ny] = True
                    elif stor[nx][ny] == carrier:
                        stor[nx][ny] = 0
                        visited[nx][ny] = True
                
                # 두 자리면 모든 것 제거
                elif len(carrier) == 2:
                    if stor[nx][ny] == carrier[0]:
                        stor[nx][ny] = 0
                    Q.append([nx, ny])
                    visited[nx][ny] = True
                    
    return stor

def solution(storage, requests):
    N = len(storage)
    M = len(storage[0])
    
    stor = []
    stor.append([0] * (M+2))
    for s in storage:
        stor.append([0] + list(s) + [0])
    stor.append([0] * (M+2))
    
    for req in requests:
        visited = [[False] * (M+2) for _ in range(N+2)]
        stor = bfs(0, 0, req, visited, stor, N, M)
    
    ans = 0
    for s in stor:
        for ss in s:
            if ss != 0:
                ans += 1
        
    return ans