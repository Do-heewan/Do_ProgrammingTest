def solution(n, lost, reserve):
    answer = 0
    rev = list(set(reserve) - set(lost))
    lst = list(set(lost) - set(reserve))
    
    for i in range(1, n+1):
        if not i in lst:
            answer += 1
    
    for l in lst:
        if l-1 in rev:
            answer += 1
            rev.remove(l-1)
            continue
        elif l+1 in rev:
            answer += 1
            rev.remove(l+1)
        
    return answer