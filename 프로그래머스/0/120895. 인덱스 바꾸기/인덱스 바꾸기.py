def solution(my_string, num1, num2):
    new_string = ''
    for i in range(len(my_string)):
        if (i == num1):
            new_string += my_string[num2]
            continue
        elif (i == num2):
            new_string += my_string[num1]
            continue
        new_string += my_string[i]
    
    return new_string