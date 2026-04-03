# 1374 강의실

import sys
input = sys.stdin.readline

import heapq

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort(key=lambda x : x[1])

heap = []
heapq.heappush(heap, lst[0][2])

cnt = 1
for i in range(1, N):
    curr_start, curr_end = lst[i][1], lst[i][2]

    if curr_start < heap[0]:
        cnt += 1
        heapq.heappush(heap, curr_end)

    else:
        heapq.heappop(heap)
        heapq.heappush(heap, curr_end)

print(cnt)