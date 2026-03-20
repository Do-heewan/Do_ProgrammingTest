def solution(schedules, timelogs, startday):
    def time_change(n):
        hh = n // 100
        mm = int(str(n)[-2:])
        rest = mm % 10
        
        if mm >= 50 and mm < 60:
            return (hh+1)*100 + rest
        else:
            return n+10
    
    answer = 0
    
    n = len(schedules)
    for i in range(n):
        isAble = True
        limit = time_change(schedules[i])
        
        for j in range(7):
            day = (j+startday-1) % 7 + 1
            if day == 6 or day == 7:
                continue
            
            curr = timelogs[i][j]
            
            if curr > limit:
                isAble = False

        if isAble:
            answer += 1
    
    return answer