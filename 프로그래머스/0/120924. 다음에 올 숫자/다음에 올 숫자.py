def solution(common):
    answer = 0
    
    if (common[1] - common[0] == common[2] - common[1]):
        return (common[-1] + common[1] - common[0])
        
    elif (common[1] // common[0] == common[2] // common[1]):
        return common[len(common) - 1] * common[1] // common[0]
    
    return answer