# 20002 사과 나무

def prefixSum(x, y):
    prefix_sum = [[0] * (x+1) for _ in range(y+1)]

    for i in range(1, x+1):
        for j in range(1, y+1):
            prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + tree[i-1][j-1]

    return prefix_sum

N = int(input())
tree = [list(map(int, input().split())) for _ in range(N)]

part_sum = -1001
prefix_sum = prefixSum(N, N)

for k in range(1, N+1):
    for i in range(1, N-k+2):
        for j in range(1, N-k+2):
            X = i + k - 1
            Y = j + k - 1
            part_sum = max(part_sum, prefix_sum[X][Y] - prefix_sum[i-1][Y] - prefix_sum[X][j-1] + prefix_sum[i-1][j-1])

print(part_sum)