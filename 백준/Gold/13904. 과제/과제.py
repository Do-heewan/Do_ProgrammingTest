# 13904 과제

import heapq

N = int(input())

todo = []
for _ in range(N):
    todo.append(list(map(int, input().split())))

todo.sort(key=lambda x : (x[0], x[1]))

heap = []
for d, w in todo:
    heapq.heappush(heap, w)

    if len(heap) > d:
        heapq.heappop(heap)    

print(sum(heap))