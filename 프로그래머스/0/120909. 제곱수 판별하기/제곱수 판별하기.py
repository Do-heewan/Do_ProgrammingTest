def solution(n):  
    num_list = [i for i in range(1, 10001)]
    
    for i in range(len(num_list)):
        if (n / num_list[i] == num_list[i]):
            return 1
    
    return 2
