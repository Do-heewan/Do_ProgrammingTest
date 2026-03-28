# 1781 컵라면

import sys
input = sys.stdin.readline

import heapq

N = int(input())
cup = [list(map(int, input().split())) for _ in range(N)]

cup.sort()

heap = []
for a, b in cup:
    heapq.heappush(heap, b)

    if len(heap) > a:
        heapq.heappop(heap)

print(sum(heap))