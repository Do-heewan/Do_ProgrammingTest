# 11286 절댓값 힙

import sys
import heapq
input = sys.stdin.readline

T = int(input())

heap = []

def abs_heap(num):
    if (num != 0):
        heapq.heappush(heap, [abs(num), num])

    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)

for _ in range(T):
    abs_heap(int(input()))