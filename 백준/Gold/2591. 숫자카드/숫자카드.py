# 2591 숫자카드

num = input()
dp = [[0] * (35) for _ in range(len(num))] # 5자리 수에서, 각 자릿수마다 어떤 숫자가 쓰이는지 체크
dp[0][int(num[0])] = 1

for i in range(1, len(num)):
    for j in range(1, 35):
        next = 10 * j + int(num[i])
        if next <= 34:
            dp[i][next] += dp[i-1][j]
        dp[i][int(num[i])] += dp[i-1][j]

print(sum(dp[-1][1:]))