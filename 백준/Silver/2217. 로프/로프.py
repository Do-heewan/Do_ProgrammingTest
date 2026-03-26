# 2217 로프

import sys
input = sys.stdin.readline

N = int(input())
lope = [int(input()) for _ in range(N)]

lope.sort()

max_value = 0
for i in range(1, N+1):
    curr = lope[-1-(i-1)]
    max_value = max(max_value, curr * i)

print(max_value)