# 7579 앱

N, M = map(int, input().split())
byte = list(map(int, input().split()))
cost = list(map(int, input().split()))

MAX_COST = sum(cost)

# dp = [0] * (MAX_COST+1)

# for i in range(N):
#     b = byte[i]
#     c = cost[i]
#     for curr_cost in range(MAX_COST, c-1, -1):
#         dp[curr_cost] = max(dp[curr_cost], dp[curr_cost-c]+b)

# for i in range(MAX_COST+1):
#     if dp[i] >= M:
#         print(i)
#         break

dp = [[0] * (MAX_COST+1) for _ in range(N+1)]

for i in range(1, N+1):
    curr_byte = byte[i-1]
    curr_cost = cost[i-1]

    for j in range(MAX_COST+1):
        if j < curr_cost:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-curr_cost]+curr_byte)

for j in range(MAX_COST+1):
    if dp[N][j] >= M:
        print(j)
        break