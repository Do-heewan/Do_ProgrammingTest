import heapq

def solution(jobs):
    n = len(jobs)
    jobs.sort(key=lambda x : x[0])
    
    answer = 0
    cnt = 0
    now = 0
    start = -1
    heap = []
    
    while cnt < n:
        for i in range(cnt, n):
            if start < jobs[i][0] <= now:
                heapq.heappush(heap, [jobs[i][1], jobs[i][0]])
                
            elif jobs[i][0] > now:
                break
                
        if heap:
            curr_dura, curr_start = heapq.heappop(heap)
            
            start = now
            now += curr_dura
            
            answer += (now - curr_start)
            cnt += 1
        else:
            now += 1
    
    return answer // n