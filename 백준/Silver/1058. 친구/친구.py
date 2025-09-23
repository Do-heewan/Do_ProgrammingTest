# 1058 친구 (BFS)

N = int(input())
graph = [list(input()) for _ in range(N)]

connected = [[0] * N for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue

            if graph[i][j] == "Y" or (graph[i][k] == "Y" and graph[k][j] == "Y"):
                connected[i][j] = 1

answer = 0
for ix in connected:
    answer = max(answer, sum(ix))

print(answer)