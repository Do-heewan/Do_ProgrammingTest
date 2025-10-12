# 12851 숨바꼭질 2

from collections import deque

def bfs(n):
    global cnt

    Q = deque()
    Q.append(n)

    while Q:
        c = Q.popleft()
        
        if c == K:
            cnt += 1
            continue

        for ix in [c-1, c+1, 2*c]:
            if 0 <= ix <= 100_000 and (time[ix] == 0 or time[ix] == time[c]+1):
                time[ix] = time[c] + 1
                Q.append(ix)

N, K = map(int, input().split())
time = [0 for _ in range(100_001)]
cnt = 0

bfs(N)
print(time[K])
print(cnt)