from itertools import combinations

def solution(n, q, ans):
    numbers = [i for i in range(1, n+1)]
    answers = list(combinations(numbers, 5))
    
    cnt = 0
    for i in range(len(q)):
        new_answers = []
        for a in answers:
            if len(set(a) & set(q[i])) == ans[i]:
                new_answers.append(a)
            
        answers = new_answers
            
    return len(new_answers)