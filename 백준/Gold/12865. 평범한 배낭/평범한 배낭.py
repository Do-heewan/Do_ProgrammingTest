# 12865 평범한 배낭

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

bag = []
for _ in range(N):
    W, V = map(int, input().split())
    bag.append([W, V])

knapsack = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        weight = bag[i-1][0]
        value = bag[i-1][1]

        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j] #weight보다 작으면 위의 값을 그대로 가져온다
        else:
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

print(knapsack[N][K])