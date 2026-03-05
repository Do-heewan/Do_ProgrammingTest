from itertools import combinations_with_replacement, permutations
import heapq

def solution(k, n, reqs):
    def calc_wait_time(queue, case):
        total_time = 0
        
        counsel_list = []
        for _ in range(case):
            heapq.heappush(counsel_list, 0)
            
        for start, duration in queue:
            curr_end = heapq.heappop(counsel_list)
            
            if curr_end < start:
                heapq.heappush(counsel_list, duration)
            
            else:
                wait_time = curr_end - start
                total_time += wait_time
                heapq.heappush(counsel_list, duration+wait_time)
                
        return total_time
    
    # 가능한 멘토 조합
    cases = set()
    for comb in combinations_with_replacement([i for i in range(1, n-k+2)], r=k):
        if sum(comb) == n:
            for perm in permutations(comb, k):
                cases.add(perm)
    
    # 각 유형별 상담시간 기준 우선순위 큐 생성
    queue = [[] for _ in range(k+1)]
    for req in reqs:
        queue[req[2]].append([req[0], req[0]+req[1]])

    result = 100_000_000
    for case in cases:
        time = 0
        for i in range(1, k+1):
            time += calc_wait_time(queue[i], case[i-1])
        result = min(result, time)
    
    return result
    
    