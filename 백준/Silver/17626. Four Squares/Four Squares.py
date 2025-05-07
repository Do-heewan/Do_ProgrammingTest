# 17626 Four Squares O(N^2)

N = int(input())

dp = [0] * (N+1)

# 제곱수의 경우 1
k = 1
while (k ** 2 <= N):
    dp[k ** 2] = 1
    k += 1

for i in range(1, N+1):
    if (dp[i] != 0): # 0이 아닌 값에 대해선 무시
        continue

    j = 1
    while (j*j <= i): # i보다 작은 제곱수에 대해
        if (dp[i] == 0): # 경우의 수가 0일 경우
            dp[i] = dp[j*j] + dp[i - j*j] # 제곱수의 경우의 수 + 제곱수를 뺀 수의 경우의 수
        else: # 경우의 수가 이미 존재할 경우
            dp[i] = min(dp[i], dp[j*j] + dp[i - j*j]) # 기존의 경우와 새로운 경우 중 작은 값

        j += 1

print(dp[N])