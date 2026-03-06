from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    def word_check(a, b):
        diff = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                diff += 1
        
        if diff == 1:
            return True
        return False

    queue = deque()
    queue.append([0, begin])
    
    while queue:
        cnt, word = queue.popleft()
        
        if word == target:
            return cnt

        for w in words:
            if word_check(word, w):
                queue.append([cnt+1, w])