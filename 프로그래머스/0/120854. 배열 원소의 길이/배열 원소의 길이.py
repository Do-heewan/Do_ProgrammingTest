def solution(strlist):
    result = []
    for word in strlist:
        word_len = 0
        for i in word:
            word_len += 1
        result.append(word_len)
        
    return result
