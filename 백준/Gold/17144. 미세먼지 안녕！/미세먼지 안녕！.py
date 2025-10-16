# 17144 미세먼지 안녕!

from collections import deque

dv = [(-1, 0), (0,1), (1,0), (0,-1)]
R, C, T = map(int, input().split())

board = [[int(x) for x in input().split()] for _ in range(R)]


def getDustPos():
    dusts = []
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                dusts.append((i,j, board[i][j]))
    
    return dusts

def getCleanerPos():
    for i in range(R):
        if board[i][0] == -1:
            return i

def getAllDusts():
    total = 0
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                total += board[i][j]
    return total

def bfs(R, C):
    global board
    queue = deque(getDustPos())

    while queue:
        x, y, v = queue.popleft()

        cnt = 0
        tmp = v // 5
        for d in dv:
            nx = x + d[0]
            ny = y + d[1]

            if nx < 0 or nx >= R or ny < 0 or ny >= C or board[nx][ny] == -1:
                continue
            
            board[nx][ny] += tmp
            cnt += 1
        
        board[x][y] -= tmp * cnt

def up_cleaner(x, y):
    global board
    v, d = 0, 1
    while True:

        nx = x + dv[d][0]
        ny = y + dv[d][1]

        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            d = (d + 3) % 4     # 반시계 방향으로 회전
            continue

        else:
            if board[nx][ny] == -1: # 이동한 곳이 공청기라면
                return
            
            tmp = board[nx][ny] # 현재 위치의 값 저장
            board[nx][ny] = v     # 이전 위치값 변경
            v = tmp             # 현재 위치에 원래 있던 값으로 업데이트
            x, y = nx, ny

def down_cleaner(x, y):
    global board
    v, d = 0, 1
    while True:

        nx = x + dv[d][0]
        ny = y + dv[d][1]

        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            d = (d + 1) % 4     # 시계 방향으로 회전
            continue

        else:
            if board[nx][ny] == -1:
                return
            tmp = board[nx][ny] # 현재 위치의 값 저장
            board[nx][ny] = v     # 이전 위치값 변경
            v = tmp             # 현재 위치에 원래 있던 값으로 업데이트
            x, y = nx, ny


cleaner_x = getCleanerPos() # 위 공청기 x좌표, y좌표

for i in range(T):

    bfs(R, C) # 먼지 동시 확산

    up_cleaner(cleaner_x, 0)
    down_cleaner(cleaner_x + 1, 0)

print(getAllDusts())