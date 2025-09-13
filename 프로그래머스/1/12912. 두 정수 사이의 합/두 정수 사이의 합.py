def solution(a, b):
    answer = 0
    if (a < b): a, b = b, a

    for i in range(b, a+1):
        answer += i
    return answer