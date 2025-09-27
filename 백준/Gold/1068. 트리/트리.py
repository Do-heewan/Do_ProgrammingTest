# 1068 트리

def dfs(n):
    tree[n] = -2
    
    for i in range(len(tree)):
        if n == tree[i]:
            dfs(i)

N = int(input())
tree = list(map(int, input().split()))
node = int(input())

dfs(node)

cnt = 0
for i in range(len(tree)):
    if tree[i] != -2 and i not in tree:
        cnt += 1

print(cnt)