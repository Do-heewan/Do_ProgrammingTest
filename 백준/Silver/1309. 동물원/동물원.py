# 1309 동물원

N = int(input())

dp = [[0] * 3 for _ in range(N)] # i번째 줄의 우리에 사자를 넣는 경우의 수는 3가지. i-1의 상태에 따라 달라진다.

for i in range(3):
    dp[0][i] = 1

for i in range(1, N):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % 9901

print(sum(dp[N-1]) % 9901)