# 1715 카드 정렬하기

import sys
input = sys.stdin.readline

import heapq

N = int(input())

total_count = 0
cards = [int(input()) for _ in range(N)]

heapq.heapify(cards)

result = []
while len(cards) != 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)

    heapq.heappush(cards, (a+b))
    result.append(a+b)

print(sum(result))