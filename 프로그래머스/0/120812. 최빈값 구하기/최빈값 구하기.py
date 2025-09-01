def solution(array):
    lst = [0] * (max(array) + 1)
    
    for ix in array:
        lst[ix] += 1
        
    cnt = 0
    for ix in lst:
        if ix == max(lst):
            cnt += 1
            
    return -1 if cnt > 1 else lst.index(max(lst))