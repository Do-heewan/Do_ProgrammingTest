# 14500 테트로미노

N, M = map(int, input().split())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

visited = [[False] * M for _ in range(N)]

maximum = 0

def dfs(x, y, tmp, cnt):
    global maximum

    if (cnt == 4):
        maximum = max(maximum, tmp)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < N) and (0 <= ny < M) and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, tmp + graph[nx][ny], cnt + 1)
            visited[nx][ny] = False

def fuck_you(x, y):
    global maximum
    arr = []

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < N) and (0 <= ny < M) and not visited[nx][ny]:
            arr.append(graph[nx][ny])

    length = len(arr)

    if (length == 4):
        arr.sort(reverse=True)
        arr.pop()
        maximum = max(maximum, sum(arr) + graph[x][y])

    elif (length == 3):
        maximum = max(maximum, sum(arr) + graph[x][y])
    
    return

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, graph[i][j], 1)
        fuck_you(i, j)
        visited[i][j] = False

print(maximum)