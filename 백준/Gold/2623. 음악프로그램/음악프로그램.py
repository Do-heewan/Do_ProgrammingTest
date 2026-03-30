# 2623 음악프로그램

from collections import deque

def topology():
    result = []

    Q = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            Q.append(i)

    while Q:
        c = Q.popleft()
        result.append(c)

        for ix in graph[c]:
            indegree[ix] -= 1

            if indegree[ix] == 0:
                Q.append(ix)   

    return result

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
for _ in range(M):
    lst = list(map(int, input().split()))
    l = lst[0]
    for i in range(1, l):
        graph[lst[i]].append(lst[i+1])
        indegree[lst[i+1]] += 1

answer = topology()

if len(answer) == N:
    for a in answer:
        print(a)
else:
    print(0)