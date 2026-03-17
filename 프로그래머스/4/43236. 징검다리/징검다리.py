from itertools import combinations

def solution(distance, rocks, n):
    answer = 0
    rocks.append(distance)
    rocks.sort()
    
    left = 1
    # right = distance
    right = max(rocks[i]-rocks[i-1] for i in range(1, len(rocks)))
    
    while left <= right:
        mid = (left + right) // 2 # 가능한 최솟값
        remove_cnt = 0 # 제거한 돌의 수
        curr = 0 # 현재 위치
        
        for r in rocks:
            if r - curr < mid:
                remove_cnt += 1
            else:
                curr = r
        
        if remove_cnt > n:
            right = mid-1
        else:
            left = mid+1
            answer = mid
        
    return answer