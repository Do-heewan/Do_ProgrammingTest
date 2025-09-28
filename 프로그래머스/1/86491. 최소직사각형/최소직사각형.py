def solution(sizes):
    for ix in sizes:
        ix.sort()
        
    max_w = 0
    max_h = 0
    for ix in sizes:
        if ix[0] > max_w:
            max_w = ix[0]
        if ix[1] > max_h:
            max_h = ix[1]
            
    return max_w * max_h