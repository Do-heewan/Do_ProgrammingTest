# 18513 샘터

from collections import deque

N, K = map(int, input().split())
pool = list(map(int, input().split()))

Q = deque()
visited = dict()

for p in pool:
    Q.append(p)
    visited[p] = 0

cnt = 0
ans = 0

while Q:
    curr = Q.popleft()

    for next_point in [curr-1, curr+1]:

        if next_point not in visited.keys():
            visited[next_point] = visited[curr] + 1
            ans += visited[next_point]
            cnt += 1

            if cnt == K:
                print(ans)
                exit()
        
            Q.append(next_point)