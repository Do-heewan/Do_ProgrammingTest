from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    field = [[-1] * (51*2) for i in range(51*2)]
    
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x : x*2, r)
        
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                # 직사각형의 내부 0으로 채우기
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0
                # 다른 직사각형의 내부가 아니면서 현재 직사각형의 테두리일 때 1로 채움
                elif field[i][j] != 0:
                    field[i][j] = 1
    
    Q = deque()
    Q.append([characterX * 2, characterY * 2])
    visited = [[1] * (51*2) for i in range(51*2)]
    visited[characterX * 2][characterY * 2] = 0
    
    while Q:
        cx, cy = Q.popleft()
        
        if cx == itemX * 2 and cy == itemY * 2:
            answer = visited[cx][cy] // 2
            break
            
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            
            # 현재 테두리 위 이고 방문하지 않은 점이라면
            if field[nx][ny] == 1 and visited[nx][ny] == 1:
                Q.append([nx, ny])
                visited[nx][ny] = visited[cx][cy] + 1
    
    return answer