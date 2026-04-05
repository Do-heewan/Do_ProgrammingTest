# 11000 강의실 배정

import sys
input = sys.stdin.readline

import heapq

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort()

heap = []
heapq.heappush(heap, lst[0][1])

cnt = 1
for i in range(1, N):
    curr_end = lst[i][1]

    if lst[i][0] < heap[0]:
        heapq.heappush(heap, curr_end)
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, curr_end)
    
print(len(heap))