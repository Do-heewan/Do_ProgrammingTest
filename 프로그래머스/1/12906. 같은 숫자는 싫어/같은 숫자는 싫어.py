def solution(arr):
    # arr = [1, 1, 3, 3, 0, 1, 1]
    
    answer = []
    for x in arr:
        if answer and answer[-1] == x:
            continue

        answer.append(x)
        
    return answer
        