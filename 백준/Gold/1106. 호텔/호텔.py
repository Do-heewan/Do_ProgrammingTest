# 1106 호텔

C, N = map(int, input().split())

INF = 1_000_000_000

hotel = []
dp = [INF] * (C+100)
dp[0] = 0

for _ in range(N):
    cost, person = map(int, input().split())
    hotel.append([cost, person])

for cost, person in hotel:
    for i in range(person, C+100):
        dp[i] = min(dp[i-person] + cost, dp[i])

print(min(dp[C:]))