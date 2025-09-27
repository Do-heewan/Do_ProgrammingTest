def solution(s):
    stack = []
    
    for ix in s:
        if ix == "(":
            stack.append(ix)
        elif ix == ")" and stack:
            stack.pop()
        else:
            return False
    
    if stack: return False
    return True
    
    
    
    
    
    
    
    
    
#     stack = []
    
#     for ix in s:
#         if ix == "(":
#             stack.append(ix)
#         elif ix == ")":
#             if not stack:
#                 return False
#             stack.pop()
            
#     if stack:
#         return False
#     return True