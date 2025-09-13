def solution(numbers):
    num_lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    answer = 0
    for ix in num_lst:
        if ix not in numbers:
            answer += ix
    
    return answer