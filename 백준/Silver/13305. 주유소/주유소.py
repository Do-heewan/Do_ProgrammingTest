# 13305 주유소

import sys
input = sys.stdin.readline

INF = 1_000_000_000

N = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))

cheap_oil = INF
total_cost = 0
for i in range(N-1):
    cheap_oil = min(cheap_oil, cost[i])

    total_cost += distance[i] * cheap_oil

print(total_cost)