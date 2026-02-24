# 1644 소수의 연속합

import math

def eratosthenes(N):
    is_prime = [True] * (N+1)
    is_prime[1] = False

    for i in range(2, int(math.sqrt(N))+1):
        if not is_prime[i]:
            continue

        for j in range(i*i, N+1, i):
            is_prime[j] = False

    primes = list(i for i in range(2, N+1) if is_prime[i])

    return primes

N = int(input())
primes = eratosthenes(N)

left = 0
right = 0
sum_val = 0

ans = 0
while True:
    if sum_val >= N:
        if sum_val == N:
            ans += 1
        sum_val -= primes[left]
        left += 1
    elif right == len(primes):
        break
    else:
        sum_val += primes[right]
        right += 1

print(ans)