# 20303 할로윈의 양아치

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

N, M, K = map(int, input().split()) # 아이들 수, 관계 수, 리미트
candy = [0] + list(map(int, input().split()))

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [i for i in range(N+1)]

for i in range(1, N+1):
    for ix in graph[i]:
        if not same_root(i, ix):
            union(i, ix)

group = {}
for i in range(1, N+1):
    root = find_root(i)
    if root not in group:
        group[root] = [0, 0]
    group[root][0] += 1
    group[root][1] += candy[i]

knapsack = list(group.values())

dp = [0] * K

for people, candy in knapsack:
    for i in range(K-1, people-1, -1):
        dp[i] = max(dp[i], dp[i-people]+candy)

print(max(dp))