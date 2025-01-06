# 1927 최소 힙

import heapq
import sys
input = sys.stdin.readline

N = int(input())

li = []
for _ in range(N):
    num = int(input())

    if (num == 0): # 힙 내 최솟값 출력
        if (len(li) == 0):
            li.append(0)
        
        print(heapq.heappop(li))
        
    else: # 힙 내 저장
        heapq.heappush(li, num)