# 1987 알파벳

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(r, c, count):
    global max_count

    max_count = max(count, max_count)
    
    for i in range(4):
        nr = r + dx[i]
        nc = c + dy[i]

        if (0 <= nr < R) and (0 <= nc < C):
            idx = ord(graph[nr][nc]) - ord('A')
            if not visited[idx]:
                visited[idx] = True
                dfs(nr, nc, count + 1)
                visited[idx] = False

R, C = map(int, input().split())

graph = []
for _ in range(R):
    graph.append([ix for ix in input()])

max_count = 0
visited = [False] * 26

start = ord(graph[0][0]) - ord('A')
visited[start] = True
dfs(0, 0, 1)

print(max_count)