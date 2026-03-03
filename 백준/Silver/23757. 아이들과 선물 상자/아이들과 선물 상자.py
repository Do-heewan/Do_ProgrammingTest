#  23757 아이들과 선물 상자

import heapq

N, M = map(int, input().split())

gift = list(map(int, input().split()))
wish = list(map(int, input().split()))

queue = [] # max-Heap으로 구현
for i in range(N):
    heapq.heappush(queue, -gift[i])

possible = True

for w in wish:
    if not queue:
        possible = False
        break
    
    largest = -heapq.heappop(queue)

    if largest < w:
        possible = False
        break

    remain = largest - w
    heapq.heappush(queue, -remain)

print(1 if possible else 0)