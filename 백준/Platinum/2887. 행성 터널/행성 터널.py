# 2887 행성 터널

N = int(input())

position = [[]]
for _ in range(N):
    x, y, z = map(int, input().split())
    position.append([x, y, z])

tree = []
# 각 축(x, y, z)에 대해 정렬한 후 인접 노드 간선만 추가
for dim in range(3):
    sorted_pos = sorted([(position[i][dim], i) for i in range(1, N+1)])
    for i in range(N - 1):
        a_idx = sorted_pos[i][1]
        b_idx = sorted_pos[i + 1][1]
        weight = abs(sorted_pos[i][0] - sorted_pos[i + 1][0])
        tree.append([a_idx, b_idx, weight])

tree.sort(key = lambda x : x[2])

parent = [i for i in range(N+1)]

def get_parent(x):
    if (parent[x] == x):
        return x

    parent[x] = get_parent(parent[x])

    return parent[x]

def union_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)

    if (a < b):
        parent[b] = a

    else:
        parent[a] = b

def same_parent(a, b):
    return get_parent(a) == get_parent(b)

answer = 0
for a, b, cost in tree:
    if not (same_parent(a, b)):
        union_parent(a, b)
        answer += cost

print(answer)