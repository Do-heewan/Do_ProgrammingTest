# 9012 괄호

T = int(input())

for _ in range(T):
    word = input()

    stack = []

    for w in word:
        if w == "(":
            stack.append(w)
        elif w == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(w)

    print("NO" if stack else "YES")