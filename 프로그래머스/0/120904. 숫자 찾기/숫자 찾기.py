# def solution(num, k):
#     num = str(num)
#     for i in range(len(num)):
#         if (num[i] == str(k)):
#             return i+1
#     return -1


def solution(num, k):
    word = str(num)
    
#     idx = 1
#     for i in word:
#         if (i == str(k)):
#             return idx
#         idx += 1

#     return -1
            
    for i in range(len(word)):
        if (word[i] == str(k)):
            return i+1
    return -1
