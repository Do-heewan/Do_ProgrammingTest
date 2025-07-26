def solution(my_string):
    lst = list(my_string.split())    
    num_list = []
    op_list = []
    
    for ix in lst:
        if ix == "+" or ix == "-":
            op_list.append(ix)
        else:
            num_list.append(ix)
            
    result = int(num_list[0])
    for i in range(len(op_list)):
        if (op_list[i] == "+"):
            result += int(num_list[i+1])
        else:
            result -= int(num_list[i+1])

    return result