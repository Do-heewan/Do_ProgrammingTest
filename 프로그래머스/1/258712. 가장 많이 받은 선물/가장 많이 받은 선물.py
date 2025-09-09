def solution(friends, gifts):
    mapping = {}
    for i in range(len(friends)):
        mapping[friends[i]] = i
    
    gift = [[0 for _ in range(len(friends))] for _ in range(len(friends))] # 리스트 초기화

    for g in gifts:
        a, b = g.split()
        gift[mapping[a]][mapping[b]] += 1
    
    # 준 선물 수
    given_gifts = []
    for i in range(len(friends)):
        given_gift = 0
        for j in gift[i]:
            given_gift += j
        given_gifts.append(given_gift)
    
    # 받은 선물 수
    taken_gifts = []
    for i in range(len(friends)):
        taken_gift = 0
        for j in range(len(friends)):
            taken_gift += gift[j][i]
        taken_gifts.append(taken_gift)
        
    score_gift = []
    for i in range(len(given_gifts)):
        score_gift.append(given_gifts[i] - taken_gifts[i])
        
    # 다음 달 받을 선물 수
    next_month = [0] * len(friends)
    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):  # (i, j) 쌍만 비교
            if gift[i][j] > gift[j][i]:
                next_month[i] += 1
            elif gift[i][j] < gift[j][i]:
                next_month[j] += 1
            else:
                if score_gift[i] > score_gift[j]:
                    next_month[i] += 1
                elif score_gift[i] < score_gift[j]:
                    next_month[j] += 1
                # 같으면 아무도 선물 받지 않음
        
    return max(next_month)
    