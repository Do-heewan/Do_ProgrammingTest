# 1697 숨바꼭질

from collections import deque

N, K = map(int, input().split())

space = [-1] * (100001)

Q = deque()
Q.append(N)
space[N] = 0

while Q:
    curr = Q.popleft()

    if curr == K:
        print(space[K])
        break

    for next in [curr-1, curr+1, 2*curr]:
        if 0 <= next < 100001 and space[next] == -1:
            space[next] = space[curr]+1
            Q.append(next)