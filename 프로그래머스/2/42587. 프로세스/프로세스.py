def solution(priorities, location):
    # stack = [1, 2, 3, 4, 5]
    # stack.pop() => 5
    # queue = [1, 2, 3, 4, 5]
    # queue.pop(0) => 1
    
    queue = []
    for i in range(len(priorities)):
        queue.append([priorities[i], i])
    
    answer = 0
    while queue:
        curr = queue.pop(0)
        # for p in queue:
        #     if curr[0] < p[0]:
        #         queue.append(curr)
        if any(curr[0] < p[0] for p in queue):
            queue.append(curr)
        else:
            answer += 1

            if curr[1] == location:
                return answer

            


    
    
        

