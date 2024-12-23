# 17466 N! mod P (1)

import sys

n, p = map(int, sys.stdin.readline().split())

num = 1

for i in range(2, n+1):
    num = (num * i) % p

print(num % p)