# 14621 나만 안되는 연애

def find_root(x):
    if x != parent[x]:
        parent[x] = find_root(parent[x])
    return parent[x]

def union(a, b):
    x = find_root(a)
    y = find_root(b)

    if x > y:
        parent[x] = y
    else:
        parent[y] = x

def same_root(x, y):
    return find_root(x) == find_root(y)

N, M = map(int, input().split())
gender = ['']+list(input().split())

edges = []
for _ in range(M):
    a, b, cost = map(int, input().split())
    
    if gender[a] != gender[b]:
        edges.append([a, b, cost])

if len(edges) < (N-1):
    print(-1)
    exit()

edges.sort(key=lambda x : x[2])

parent = [i for i in range(N+1)]

route = 0
cnt = 0
for a, b, c in edges:
    if not same_root(a, b):
        union(a, b)
        route += c
        cnt += 1

print(route if cnt == N-1 else -1)