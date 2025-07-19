def solution(my_string):
    my_string = my_string.lower()

    my_string = sorted(my_string)
    
    answer = ''
    for i in my_string:
        answer += i
    
    return answer
