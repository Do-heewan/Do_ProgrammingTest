def find_root(x):
    if x != parent[x]: parent[x] = find_root(parent[x])
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

N = int(input())
M = int(input())

parent = [i for i in range(N)]

edges = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j: continue
        if edges[i][j] == 1:
            union(i, j)

plan = list(map(int, input().split()))

isAble = True
for i in range(len(plan)-1):
    s, e = plan[i]-1, plan[i+1]-1
    if not same_root(s, e):
        isAble = False

print("YES" if isAble else "NO")