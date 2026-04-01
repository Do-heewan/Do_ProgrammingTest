# 1890 점프

def dfs(x, y):
    if x == N-1 and y == N-1:
        return 1
    
    if visited[x][y] != -1:
        return visited[x][y]
    
    visited[x][y] = 0

    jump = graph[x][y]
    for nx, ny in [[x+jump, y], [x, y+jump]]:
        if 0 <= nx < N and 0 <= ny < N:
            visited[x][y] += dfs(nx, ny)

    return visited[x][y]

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

visited = [[-1] * N for _ in range(N)]

print(dfs(0, 0))