import heapq

def solution(N, paths, gates, summits):
    INF = 100_000_000
        
    graph = [[] for _ in range(N+1)]
    
    for a, b, cost in paths:
        graph[a].append([b, cost])
        graph[b].append([a, cost])
    
    is_summit = [False] * (N+1)
    for s in summits:
        is_summit[s] = True
    
    heap = []
    weight = [INF] * (N+1)
    for g in gates:
        weight[g] = 0
        heapq.heappush(heap, [0, g])
        
    while heap:
        wgt, curr = heapq.heappop(heap)
        
        if wgt > weight[curr] or is_summit[curr]:
            continue
            
        for next_, c in graph[curr]:
            cost = max(c, weight[curr])
            if weight[next_] > cost:
                weight[next_] = cost
                heapq.heappush(heap, [cost, next_])
                
    answer = [-1, INF]
    for s in sorted(summits):
        if weight[s] < answer[1]:
            answer[0] = s
            answer[1] = weight[s]
            
    return answer