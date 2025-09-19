# 1010 다리 놓기

import math

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    # nCr = fact(n) / fact(n-r) * fact(r)
    result = math.factorial(M) / (math.factorial(M-N) * math.factorial(N))

    print(int(result))