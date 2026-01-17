# 9328 열쇠

from collections import deque, defaultdict

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    Q = deque()
    Q.append([x, y])
    visited[x][y] = True

    while Q:
        currX, currY = Q.popleft()

        for i in range(4):
            nextX = currX + dx[i]
            nextY = currY + dy[i]

            # 매트릭스 범위 안에 존재하고 벽이 아닐경우 전진
            if 0 <= nextX < N+2 and 0 <= nextY < M+2 and matrix[nextX][nextY] != "*" and not visited[nextX][nextY]:
                # 문을 만났을 때, 열쇠를 가지고 있다면
                if "A" <= matrix[nextX][nextY] <= "Z":
                    if matrix[nextX][nextY].lower() in keys:
                        # 해당 지점 방문 후 탐색 이어 나가기
                        visited[nextX][nextY] = True
                        Q.append([nextX, nextY])
                    
                    # 열쇠가 없어서 열지 못하다면 해당 지점 저장
                    else:
                        door[matrix[nextX][nextY].lower()].append([nextX, nextY])
                        continue

                # 열쇠라면 저장
                elif "a" <= matrix[nextX][nextY] <= "z":
                    key = matrix[nextX][nextY]
                    if key not in keys:
                        keys.add(key)

                        for x, y in door[key]:
                            visited[x][y] = True
                            Q.append([x, y])

                    door[key].clear()
                    visited[nextX][nextY] = True
                    Q.append([nextX, nextY])

                # 문서라면 훔치기
                elif matrix[nextX][nextY] == "$":
                    dollar.append([nextX, nextY])

                    visited[nextX][nextY] = True
                    Q.append([nextX, nextY])

                else:
                    visited[nextX][nextY] = True
                    Q.append([nextX, nextY])

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    matrix = []
    matrix.append(["."] * (M+2))
    for _ in range(N):
        matrix.append(["."] + list(input()) + ["."])
    matrix.append(["."] * (M+2))

    key_input = input().strip()
    keys = set() if key_input == "0" else set(key_input) # 현재 보유중인 열쇠 저장 셋 / "0"을 입력받으면 빈 셋
    visited = [[False] * (M+2) for _ in range(N+2)] # 방문처리
    dollar = [] # 서류 획득
    door = defaultdict(list) # 문 앞에 대기중인 위치

    bfs(0, 0)

    print(len(dollar))