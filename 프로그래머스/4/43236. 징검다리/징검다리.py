from itertools import combinations

[0, 2, 11, 14, 17, 21, 25]
[2, 9, 3, 3, 4, 4]

def solution(distance, rocks, n):
    rocks.append(distance)
    rocks.sort()
    
    left = 1
    right = distance
    
    while left <= right:
        mid = (left + right) // 2
        remove_cnt = 0
        curr = 0
        
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