import sys
input = sys.stdin.readline

n , m , k , x = map(int, input().split())
g = [[] for _ in range(n+1)]
for i in range(m):
    a , b = map(int, input().split())
    g[a].append(b)
visited = [-1] * (n+1)
visited[x] = 0
now = [x]
next = list()

for i in range(k):
    for j in now:
        for p in g[j]:
            if visited[p] == -1:
                visited[p] = i + 1
                next.append(p)
    # print(next)
    now = list(next)
    next = list()

result = []
for i in now:
    if visited[i] == k:
        result.append(i)

if result:
    result.sort()  # 오름차순 정렬
    for city in result:
        print(city)
else:
    print(-1)