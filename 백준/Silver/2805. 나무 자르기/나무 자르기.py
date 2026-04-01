# 2805 나무 자르기

N, M = map(int, input().split())
tree = list(map(int, input().split()))
tree.sort()

left, right = 1, max(tree)

answer = 0
while left <= right:
    mid = (left+right) // 2

    cut = 0
    for t in tree:
        if t < mid: continue
        cut += t - mid

    if cut >= M:
        answer = mid
        left = mid+1
    else:
        right = mid-1

print(answer)