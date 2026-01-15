# 2248 이진수 찾기

N, L, I = map(int, input().split())

dp = [[0] * (L+1) for _ in range(N+1)]

dp[0][0] = 1

# i자리수, 1의 개수가 j인 수의 개수를 구하는 dp
for i in range(1, N+1):
    dp[i][0] = 1
    for j in range(1, L+1):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

answer = ''
for i in range(N-1, -1, -1):
    if I > sum(dp[i][:L+1]): # i개 자릿수의 개수가 I번째의 수가 해당 범위안에 드는지
        answer += '1' # 아니라면 1을 앞에 붙인다.
        I -= sum(dp[i][:L+1])
        L -= 1

    else:
        answer += '0' # i개 자릿수들에 포함이 되기에 0을 붙인다.

print(answer)