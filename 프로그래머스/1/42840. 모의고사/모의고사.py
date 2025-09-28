def solution(answers):
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2 ,5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    scores = [0] * len(patterns)
    for i, ans in enumerate(answers):
        for idx, p in enumerate(patterns):
            if p[i % len(p)] == ans:
                scores[idx] += 1
                
    max_score = max(scores)
    
    answer = []
    for idx, s in enumerate(scores):
        if s == max_score:
            answer.append(idx+1)
            
    return answer

    
    
                    