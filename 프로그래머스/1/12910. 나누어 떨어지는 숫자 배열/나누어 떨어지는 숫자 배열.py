def solution(arr, divisor):
    answer = []
    for ix in arr:
        if ix % divisor == 0:
            answer.append(ix)
    answer.sort()
    if answer:
        return answer
    return [-1]