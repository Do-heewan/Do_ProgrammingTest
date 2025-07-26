def solution(babbling):
    word = ["aya", "ye", "woo", "ma"]
    
    result = []
    for ix in babbling:
        for rp in word:
            ix = ix.replace(rp, "1")
        result.append(ix)
    
    count = 0
    for ix in result:
        if set(ix) == {'1'}:
            count += 1
            
    return count