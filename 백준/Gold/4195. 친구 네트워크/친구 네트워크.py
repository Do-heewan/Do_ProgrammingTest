# 4195 친구 네트워크

def find_root(x):
    if x == parent[x]: return x
    parent[x] = find_root(parent[x])
    return parent[x]

def union(a, b):
    x = find_root(a)
    y = find_root(b)

    if x != y:
        parent[y] = x
        size[x] += size[y]

    return size[x]

def same_root(x, y):
    return find_root(x) == find_root(y)

T = int(input())

for _ in range(T):
    F = int(input())

    friends = {}
    id = 0

    parent = []
    size = []

    for _ in range(F):
        a, b = input().split()

        for name in (a, b):
            if name not in friends:
                friends[name] = id
                parent.append(id)
                size.append(1)
                id += 1

        res = union(friends[a], friends[b])
        print(res)