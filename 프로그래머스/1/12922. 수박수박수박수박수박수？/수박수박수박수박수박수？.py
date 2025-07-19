def solution(n):
    answer = ''
    while n > 0:
        if n % 2 == 1:
            answer += "수"
        else:
            answer += '박'
        
        n -= 1
        
    answer = ''.join(reversed(answer))
    return answer