def solution(my_string, n):
    answer = ''
    for ix in my_string:
        for _ in range(n):
            answer += ix
    return answer