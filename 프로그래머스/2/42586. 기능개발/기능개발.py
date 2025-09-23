from collections import deque

def solution(progresses, speeds):
    
    l = len(progresses)
    
    days = []
    for i in range(l):
        day = 0
        
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            day += 1
    
        days.append(day)
    
    target = days[0]
    answer = []
    count = 1

    for d in days[1:]:
        if d <= target:
            count += 1
        else:
            answer.append(count)
            count = 1
            target = d

    answer.append(count)
            
    return answer