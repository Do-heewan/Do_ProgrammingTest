# 1202 보석 도둑

import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
jewel = [list(map(int, input().split())) for _ in range(N)]
knapsack = [int(input()) for _ in range(K)]

jewel.sort() # 오름차순 (가벼운 보석 부터)
knapsack.sort() # 오름차순 (가방의 무게가 작은 것 부터)

heap = []
result = 0
for k in knapsack:
    while jewel and jewel[0][0] <= k:
        heapq.heappush(heap, -jewel[0][1])
        heapq.heappop(jewel)

    if heap:
        result -= heapq.heappop(heap)

print(result)