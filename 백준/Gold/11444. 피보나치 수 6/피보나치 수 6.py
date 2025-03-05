# 11444 피보나치 수 6

import sys
sys.setrecursionlimit(10**8)

N = int(input())
mod = 1_000_000_007

fib = {0 : 0, 1 : 1, 2 : 1}
def fibo(num):
    if num not in fib:
        if (num % 2 == 0): # num이 짝수인 경우
            fib[num] = (fibo(num // 2 )* (fibo(num // 2) + 2 * fibo(num // 2 - 1))) % mod
        else: # num이 홀수인 경우
            fib[num] = ((fibo(num // 2)) ** 2 + (fibo(num // 2 + 1)) ** 2) % mod

    return fib[num]

print(fibo(N))