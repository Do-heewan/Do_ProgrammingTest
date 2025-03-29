# 11279 최대 힙

import heapq
import sys
input = sys.stdin.readline

N = int(input())

stack = []
def search(num):
    if (num == 0):
        if (len(stack) == 0):
            heapq.heappush(stack, (0, 0))
        result = heapq.heappop(stack)[1]
        print(result)

    else:
        heapq.heappush(stack, (-num, num))

for _ in range(N):
    search(int(input()))