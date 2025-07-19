# def solution(array):
#     word = []
#     for ix in array:
#         ix = str(ix)
#         for il in ix:
#             word.append(il)
#     answer = 0
#     for ix in word:
#         if (ix == "7"):
#             answer += 1
    
#     return answer
            
    
    
    
    
    
    
    
    
def solution(array):
    count = 0
    for ix in array:
        ix = str(ix)
        
        for ixx in ix:
            if (ixx == "7"):
                count += 1
    
    return count






