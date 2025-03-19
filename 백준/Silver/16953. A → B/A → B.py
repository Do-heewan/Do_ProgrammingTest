# 16953 A → B

from collections import deque

A, B = map(int, input().split())

def bfs(start, end):
    count = 1

    Q = deque()
    Q.append([start, count])

    while Q:
        c, t = Q.popleft()

        for ix in [2 * c, int(str(c) + "1")]:
            if (ix == end):
                return t+1
            
            if (ix < end):
                Q.append([ix, t + 1])

result = bfs(A, B)
print(result if result != None else -1)