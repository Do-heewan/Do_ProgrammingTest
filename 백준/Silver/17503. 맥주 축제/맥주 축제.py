# 17503 맥주 축제

import heapq
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

# 맥주 종류 순으로 (선호도, 도수)
beers = []
for _ in range(K):
    v, c = map(int, input().split())
    beers.append((v, c))

beers.sort(key = lambda x : x[1])

flavor = 0
heap = []

for beer in beers:
    if (len(heap) < N):
        heapq.heappush(heap, beer)
        flavor += beer[0]

        if (len(heap) == N):
            if (flavor >= M):
                print(beer[1])
                break
            else:
                flavor -= heapq.heappop(heap)[0]

else:
    print(-1)
