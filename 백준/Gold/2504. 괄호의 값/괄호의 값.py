# 2504 괄호의 값

word = input()

stack = []

answer = 0
tmp = 1
for i in range(len(word)):
    if word[i] == "(":
        stack.append(word[i])
        tmp *= 2

    elif word[i] == "[":
        stack.append(word[i])
        tmp *= 3

    elif word[i] == ")":
        if not stack or stack[-1] == "[":
            answer = 0
            break

        if word[i-1] == "(":
            answer += tmp

        stack.pop()
        tmp //= 2
        
    elif word[i] == "]":
        if not stack or stack[-1] == "(":
            answer = 0
            break

        if word[i-1] == "[":
            answer += tmp

        stack.pop()
        tmp //= 3

print(answer if not stack else 0)