def solution(info, n, m):
    answer = 10 ** 8
    
    k = len(info)
    check = set()
    
    def search(a_cnt, b_cnt, i=0):
        nonlocal answer, n, m
        
        if a_cnt >= n or b_cnt >= m:
            return
        
        if (a_cnt, b_cnt, i) in check:
            return
        
        check.add((a_cnt, b_cnt, i))
        
        if i == k:
            answer = min(answer, a_cnt)
            return
        
        na = a_cnt + info[i][0]
        nb = b_cnt + info[i][1]
    
        search(na, b_cnt, i+1)
        search(a_cnt, nb, i+1)
        
    search(0, 0, 0)
    
    if answer >= n:
        return -1
    else:
        return answer