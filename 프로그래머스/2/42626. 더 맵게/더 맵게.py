import heapq

def solution(scoville, K):
    cnt = 0
    scoville.sort()
    
    while scoville:
        first = heapq.heappop(scoville)
        
        if first >= K:
            break
        
        if scoville:
            second = heapq.heappop(scoville)

            calc = (first + second*2)
            heapq.heappush(scoville, calc)
            cnt += 1

        else:
            cnt = -1
            break
        
    return cnt
        