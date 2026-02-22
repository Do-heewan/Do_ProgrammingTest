import sys
sys.setrecursionlimit(2500) # 재귀 깊이 설정

def dfs(x, y):
    # 사이클 발견!
    if visited[x][y]:
        print("-1")
        exit()
    
    # 이미 계산된 결과가 있다면 리턴 (메모이제이션)
    if dp[x][y] != -1:
        return dp[x][y]
    
    visited[x][y] = True
    dp[x][y] = 0 # 현재 칸에서 갈 수 있는 곳이 없을 때를 위한 초기화
    
    jump = int(board[x][y])
    
    for i in range(4):
        nx = x + dx[i] * jump
        ny = y + dy[i] * jump
        
        # 범위를 벗어나거나 구멍('H')을 만나면 무시
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] != 'H':
            # 다음 칸에서 갈 수 있는 최대값 + 1
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
            
    visited[x][y] = False # 백트래킹: 탐색 종료 후 방문 해제
    return dp[x][y]

# 입력부
N, M = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

dp = [[-1] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]

# 0,0에서 시작 (최초 시작도 이동 횟수에 포함하므로 결과에 +1 필요)
print(dfs(0, 0) + 1)