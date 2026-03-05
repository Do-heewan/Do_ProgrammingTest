# 1449 수리공 항승

N, L = map(int, input().split())
position = list(map(int, input().split()))
position.sort()

dp = [-1] * (1001)
dp[0] = 0

tape = 0
for i in position:
    if dp[i] == -1:
        for j in range(i, i+L):
            if j > 1000:
                continue
            dp[j] = 0
        tape += 1

print(tape)