# 2342 Dance Dance Revolution

INF = 100_000_000

def move(curr, next):
    if curr == 0:
        return 2
    elif curr == next:
        return 1
    elif abs(curr - next) == 2:
        return 4
    else:
        return 3

lst = list(map(int, input().split()))
lst.pop()
N = len(lst)

# dp[i][l][r] : i번째 밟을 차례에서, 왼발로 l을 밟고있고, 오른발로 r을 밟고 있을 때 까지의 최소 힘
dp = [[[INF for _ in range(5)] for _ in range(5)] for _ in range(N+1)]
dp[0][0][0] = 0

for k in range(N):
    next_ = lst[k]
    for i in range(5):
        for j in range(5):
            curr = dp[k][i][j]

            if curr == INF: continue

            dp[k+1][next_][j] = min(dp[k+1][next_][j], curr + move(i, next_))
            dp[k+1][i][next_] = min(dp[k+1][i][next_], curr + move(j, next_))

ans = INF
for l in range(5):
    for r in range(5):
        ans = min(ans, dp[N][l][r])

print(ans)