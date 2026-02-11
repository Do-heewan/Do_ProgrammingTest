# 9020 골드바흐의 추측

import math

N = 10000
is_prime = [True] * (N+1)
is_prime[1] = False

for i in range(2, int(math.sqrt(N))+1):
    if not is_prime:
        continue

    for j in range(2*i, N+1, i):
        is_prime[j] = False

primes = set(i for i in range(2, N+1) if is_prime[i])

T = int(input())

for _ in range(T):
    num = int(input())

    l = r = num // 2

    while True:
        if l in primes and r in primes:
            break

        l -= 1
        r += 1
    
    print(l ,r)