# 15652 N과 M (4)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

s = []

def dfs(x): # 앞의 숫자와 비교해야하므로 파라미터로 넘겨줌
    if len(s) == M: # s의 길이가 m과 같으면 답 출력
        print(*s)
        return

    for i in range(x,N+1): # 파라미터로 받은 숫자보다 같거나 커야함
        s.append(i) # 수를 더해주고
        dfs(i) # 더한 수를 파라미터로 가지고 dfs
        s.pop() # 원 상태로 돌리기 위해 pop

dfs(1)