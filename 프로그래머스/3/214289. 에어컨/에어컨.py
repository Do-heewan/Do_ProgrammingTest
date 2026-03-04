def solution(temperature, t1, t2, a, b, onboard):
    # -10 ~ 40 -> 0 ~ 50으로 치환
    OFFSET = 10
    MAX_TEMP = 50
    INF = 100_000_000
    
    t1 += OFFSET
    t2 += OFFSET
    outside = temperature + OFFSET
    
    time = len(onboard)
    
    # dp[i][j] = i분일때 j의 온도가 되기 위한 최소 전력
    dp = [[INF] * (MAX_TEMP+1) for _ in range(time)]
    dp[0][outside] = 0

    for i in range(time-1):
        for curr_temp in range(MAX_TEMP + 1):
            if dp[i][curr_temp] == INF:
                continue
                
            curr_cost = dp[i][curr_temp]
            
            # 에어컨 off
            if curr_temp < outside:
                next_temp = curr_temp + 1
            elif curr_temp > outside:
                next_temp = curr_temp - 1
            else:
                next_temp = curr_temp
                
            if 0 <= next_temp <= MAX_TEMP:
                # 손님이 있는 경우 온도 제한
                if onboard[i+1] == 0 or (t1 <= next_temp <= t2):
                    dp[i+1][next_temp] = min(dp[i+1][next_temp], curr_cost)
                    
            # 에어컨 on (온도 유지)
            next_temp = curr_temp
            if onboard[i+1] == 0 or (t1 <= next_temp <= t2):
                dp[i+1][next_temp] = min(dp[i+1][next_temp], curr_cost+b)
            
            # 에어컨 on (1도 하강)
            if curr_temp - 1 > 0:
                next_temp = curr_temp - 1
                if onboard[i+1] == 0 or (t1 <= next_temp <= t2):
                    dp[i+1][next_temp] = min(dp[i+1][next_temp], curr_cost+a)
                
            # 에어컨 on (1도 상승)
            if curr_temp + 1 < MAX_TEMP:
                next_temp = curr_temp + 1
                if onboard[i+1] == 0 or (t1 <= next_temp <= t2):
                    dp[i+1][next_temp] = min(dp[i+1][next_temp], curr_cost+a)
            
    last_guest = 0
    for i in range(time-1, -1, -1):
        if onboard[i] == 1:
            last_guest = i
            break
            
    answer = min(dp[last_guest][t1:t2+1])
    
    return answer
            