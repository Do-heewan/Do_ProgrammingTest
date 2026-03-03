# 1765 닭싸움 팀 정하기

from collections import deque

def bfs(n):
    if visited[n]:
        return 0

    Q = deque()
    Q.append(n)
    visited[n] = True

    while Q:
        c = Q.popleft()

        for ix in F[c]:
            if not visited[ix]:
                visited[ix] = True
                Q.append(ix)

    return 1

N = int(input())
M = int(input())

F = [[] for _ in range(N+1)]
E = [[] for _ in range(N+1)]
for _ in range(M):
    w, a, b = input().split()

    if w == "F":
        F[int(a)].append(int(b))
        F[int(b)].append(int(a))
    elif w == "E":
        E[int(a)].append(int(b))
        E[int(b)].append(int(a))

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j: continue

        if list(set(E[i]) & set(E[j])):
            F[i].append(j)

visited = [False] * (N+1)

ans = 0
for i in range(1, N+1):
    ans += bfs(i)

print(ans)