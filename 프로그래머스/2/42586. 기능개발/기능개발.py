from collections import deque

def solution(progresses, speeds):
    
    Q_p = deque(progresses)
    Q_s = deque(speeds)
    
    answer = []
    
    while Q_p:
        cnt = 0
        
        for i in range(len(Q_p)):
            Q_p[i] += Q_s[i]
            
        while Q_p and Q_p[0] >= 100:
            Q_p.popleft()
            Q_s.popleft()
            cnt += 1
            
        if cnt > 0:
            answer.append(cnt)
            
    return answer
            
    
    
#     answer = []
    
#     while progresses:
#         cnt = 0
        
#         for i in range(len(progresses)):
#             progresses[i] += speeds[i]
            
#         while progresses and progresses[0] >= 100:
#             progresses.pop(0)
#             speeds.pop(0)
#             cnt += 1
        
#         if cnt > 0: answer.append(cnt)

#     return answer
    
    
    


#     answer = []
#     Q = deque(progresses)
    
#     while Q:
#         day = 0
        
#         while Q and Q[0] >= 100:
#             Q.popleft()
#             speeds.pop(0)
#             day += 1
            
#         Q = deque(Q[i] + speeds[i] for i in range(len(Q)))
        
#         if day > 0:
#             answer.append(day)
        
#     return answer

