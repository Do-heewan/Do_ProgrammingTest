# 9251 LCS

word = input()
target = input()

W = len(word)
T = len(target)

dp = [[0] * (T+1) for _ in range(W+1)] # dp[i][j] w단어의 i까지 단어와 t단어의 j까지의 단어에서 최장공통부분

for i in range(1, W+1):
    for j in range(1, T+1):
        if word[i-1] == target[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[W][T])