# 20922 겹치는 건 싫어

N, M = map(int, input().split())
lst = list(map(int, input().split()))

visited = [0] * 100001

start = 0
answer = 0

for end in range(N):
    visited[lst[end]] += 1

    while visited[lst[end]] > M:
        visited[lst[start]] -= 1
        start += 1
    
    answer = max(answer, end-start+1)

print(answer)