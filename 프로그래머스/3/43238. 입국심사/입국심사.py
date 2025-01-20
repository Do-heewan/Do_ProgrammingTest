def solution(n, times):
    start = min(times)
    end = max(times) * n
    
    while (start <= end):
        mid = (start + end) // 2
        
        people = 0
        for time in times:
            people += mid // time
            
            if (people >= n):
                break
        
        # n명 초과 심사했다면, 시간이 너무 많은 것
        # 딱 n명 심사했더라도, 시간이 남을 가능성 있음
        if (people >= n):
            answer = mid
            end = mid -1

        # n명 미만 심사했다면, 시간이 너무 부족하다
        else:
            start = mid + 1
        
    return answer