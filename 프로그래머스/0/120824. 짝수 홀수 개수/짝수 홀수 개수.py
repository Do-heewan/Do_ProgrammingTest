def solution(num_list):
    answer = [0, 0]
    for ix in num_list:
        if ix % 2 == 0:
            answer[0] += 1
        else:
            answer[1] += 1
    return answer