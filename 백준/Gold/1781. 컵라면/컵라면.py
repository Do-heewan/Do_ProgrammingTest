# 1781 컵라면

import sys
input = sys.stdin.readline

import heapq

N = int(input())

test = []
for _ in range(N):
    test.append(list(map(int, input().split())))

test.sort(key=lambda x : x[0])

heap = []
for a, b in test:
    heapq.heappush(heap, b)

    if len(heap) > a:
        heapq.heappop(heap)

print(sum(heap))