def solution(slice, n):
#     answer = 0
#     while n > 0:
#         n -= slice
#         answer += 1
        
#     return answer

    cnt = 1
    while True:
        if (cnt * slice >= n):
            break
        cnt += 1
    return cnt