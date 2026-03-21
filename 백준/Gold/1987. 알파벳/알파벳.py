# 1987 알파벳

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(x, y, visited):
    global answer
    answer = max(answer, len(visited))

    if answer == 26:
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < R and 0 <= ny < C:
            next_ = graph[nx][ny]
            if next_ not in visited:
                visited.add(next_)
                dfs(nx, ny, visited)
                visited.remove(next_)

R, C = map(int, input().split())

graph = []
for _ in range(R):
    graph.append(list(input()))

answer = 0
dfs(0, 0, set(graph[0][0]))

print(answer)