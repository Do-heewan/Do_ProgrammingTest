# 16724 피리 부는 사나이

def move(x, y, dir):
    if dir == "U":
        return (x-1, y)
    elif dir == "D":
        return (x+1, y)
    elif dir == "L":
        return (x, y-1)
    elif dir == "R":
        return (x, y+1)

def dfs(x, y, group):
    visited[x][y] = group
    
    nx, ny = move(x, y, graph[x][y])

    if visited[nx][ny] == -1:
        return dfs(nx, ny, group)

    if visited[nx][ny] == group:
        return 1

    return 0

N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]

visited = [[-1] * M for _ in range(N)]

ans = 0
group = 0
for x in range(N):
    for y in range(M):  
        if visited[x][y] == -1:
            ans += dfs(x, y, group)
            group += 1

print(ans)