# 11279 최대 힙

import heapq
import sys
input = sys.stdin.readline

N = int(input())

heap = []
def search(num):
    if (num == 0):
        if (len(heap) == 0):
            heapq.heappush(heap, (0, 0))
        result = heapq.heappop(heap)[1]
        print(result)

    else:
        heapq.heappush(heap, (-num, num))

for _ in range(N):
    search(int(input()))