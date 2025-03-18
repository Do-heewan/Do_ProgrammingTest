# 15666 N과 M (12)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
seq = list(set(map(int, input().split()))) # set 중복 제거 수열 입력
seq.sort()

s = []
def dfs(x):
    if (len(s) == M):
        print(*s)
        return
    
    for i in range(x, len(seq)):
        s.append(seq[i])
        # print(f"현재 상태 : {s}")
        dfs(i)
        s.pop()

dfs(0)