# 11047 동전 0

N, K = map(int, input().split())

coin = []
for _ in range(N):
    coin.append(int(input()))

coin.sort(reverse=True)

res = 0
for c in coin:
    if c > K:
        continue
    calc = K // c
    K %= c
    res += calc

print(res)