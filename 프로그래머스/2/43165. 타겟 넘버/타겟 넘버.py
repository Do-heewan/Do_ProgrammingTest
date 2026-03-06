answer = 0

def dfs(numbers, target, curr, idx):
    global answer
        
    if len(numbers) == idx:
        if curr == target:
            answer += 1
        return

    dfs(numbers, target, curr-numbers[idx], idx+1)
    dfs(numbers, target, curr+numbers[idx], idx+1)

def solution(numbers, target):  
    dfs(numbers, target, 0, 0)
    
    return answer