def solution(name):
    answer = 0
    n = len(name)
    
    for c in name:
        answer += min(ord(c)-ord('A'), ord('Z')-ord(c)+1)
    
    move = n-1
    
    for i in range(n):
        next_i = i+1
        
        while next_i < n and name[next_i] == 'A':
            next_i += 1
            
        move = min(move, 2*i + n-next_i, i + 2*(n-next_i))
        
    return answer + move