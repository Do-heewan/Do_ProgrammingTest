# 28707 배열 정렬

import heapq

INF = 10_000_000

def swap(tup, left, right):
    lst = list(tup)
    lst[left], lst[right] = lst[right], lst[left]
    return tuple(lst)

def dijkstra(tup):
    queue = []
    heapq.heappush(queue, [0, tup])
    weight[tup] = 0

    while queue:
        cost, curr_tup = heapq.heappop(queue)

        for l, r, c in graph:
            next_tup = swap(curr_tup, l, r)

            if weight.get(next_tup) is None or weight[next_tup] > cost + c:
                weight[next_tup] = cost + c
                heapq.heappush(queue, [weight[next_tup], next_tup])

N = int(input())
arr = [0] + list(map(int, input().split()))
tup_arr = tuple(arr)
M = int(input())

graph = []
for _ in range(M):
    a, b, cost = map(int, input().split())
    graph.append([a, b, cost])

weight = dict()

dijkstra(tup_arr)

res = tuple(sorted(arr))

print(weight[res] if res in weight else -1)