# 10799 쇠막대기

import sys
input = sys.stdin.readline

word = input()

stack = []

cnt = 0
total = 0
for w in word:
    if w == "(":
        stack.append(w)
        cnt += 1

    elif w == ")" and stack[-1] == "(":
        stack.append(w)
        cnt -= 1
        total += cnt
    
    elif w == ")" and stack[-1] == ")":
        stack.append(w)
        total += 1
        cnt -= 1

print(total)