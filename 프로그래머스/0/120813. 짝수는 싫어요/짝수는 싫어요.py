def solution(n):
    answer = []
    for i in range(n, 0, -1):
        if (i % 2 == 1):
            answer.append(i)
    answer.sort()
    
    return answer