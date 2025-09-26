# 13172 Σ

MOD = 1_000_000_007

import math

M = int(input())

answer = 0
for _ in range(M):
    a, b = map(int, input().split())
    a, b = a // math.gcd(a, b), b // math.gcd(a, b)

    answer += b * pow(a, -1, MOD) % MOD
print(answer % MOD)