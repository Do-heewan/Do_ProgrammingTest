def solution(players, m, k):
#     max_player = [m-1] * 29
#     curr_server = [0] * 29
#     result = 0
    
#     for i in range(len(players)):
#         cnt = 0
        
#         if max_player[i] < players[i]:
#             cnt += players[i] // m - curr_server[i]
            
#             for j in range(i, i+k):
#                 max_player[j] += m * cnt
#                 curr_server[j] += cnt
        
#         result += cnt

#     return result

    server = [0] * 24
    answer = 0
    
    for i in range(24):
        s = players[i] // m # 서버 증설 개수
        
        if s > server[i]: # 현재 증설된 서버 수 보다 많다면
            temp = s - server[i] # 추가 증설
            answer += temp # 횟수 저장
            
            if i + k < 24:
                for j in range(i, i+k):
                    server[j] += temp
        
            else:
                for j in range(i, 24):
                    server[j] += temp
            
        
    return answer