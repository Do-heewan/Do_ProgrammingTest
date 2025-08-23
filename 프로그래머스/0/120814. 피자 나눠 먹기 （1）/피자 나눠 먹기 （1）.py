def solution(n):
    # answer = 0
    # while (n > 0):
    #     n -= 7
    #     answer += 1
    
    answer = n // 7
    if (n % 7 > 0):
        answer += 1
    
    return answer