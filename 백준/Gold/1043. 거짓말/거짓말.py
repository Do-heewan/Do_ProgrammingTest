# 1043 거짓말

def find_root(x):
    if x == parent[x]: return x
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
real = list(map(int, input().split()))
party = [list(map(int, input().split())) for _ in range(M)]

parent = [i for i in range(N+1)]

# 1. 파티 사람들간의 관계 형성
for p in party:
    for i in range(2, len(p)):
        union(p[1], p[i])

# 2. 진실을 아는 사람 추출
truth_people = set(find_root(x) for x in real[1:])

# 3. 각 파티 검사
cnt = 0
for p in party:
    if not p[1:]: continue

    if find_root(p[1]) not in truth_people:
        cnt += 1

print(cnt)