# 7579 앱

N, M = map(int, input().split())
byte = list(map(int, input().split()))
cost = list(map(int, input().split()))

MAX_COST = sum(cost)

dp = [0] * (MAX_COST+1)

for i in range(N):
    b = byte[i]
    c = cost[i]
    for curr_cost in range(MAX_COST, c-1, -1):
        dp[curr_cost] = max(dp[curr_cost], dp[curr_cost-c]+b)

for i in range(MAX_COST+1):
    if dp[i] >= M:
        print(i)
        break