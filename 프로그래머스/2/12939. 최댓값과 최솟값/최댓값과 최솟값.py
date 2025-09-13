def solution(s):
    num_lst = list(map(int, s.split()))
    num_lst.sort()
    
    answer = str(min(num_lst)) + " " + str(max(num_lst))
    
    return answer