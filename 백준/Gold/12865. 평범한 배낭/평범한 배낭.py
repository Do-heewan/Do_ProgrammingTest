# 12865 평범한 배낭

N, K = map(int, input().split())

items = []
for _ in range(N):
    w, v = map(int, input().split())
    items.append([w, v])

knapsack = [0] * (K+1)
for w, v in items:
    for i in range(K, w-1, -1):
        knapsack[i] = max(knapsack[i], knapsack[i-w] + v)

print(max(knapsack))