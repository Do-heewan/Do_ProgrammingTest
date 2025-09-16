def solution(number, k):
    stack = []
    
    for ix in number:
        while stack and stack[-1] < ix and k > 0:
            stack.pop()
            k -= 1
        
        stack.append(ix)
        
    if k > 0: stack = stack[:-k]

    return ''.join(stack)