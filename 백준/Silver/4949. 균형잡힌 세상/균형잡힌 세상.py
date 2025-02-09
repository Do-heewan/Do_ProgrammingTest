# 4949 균형잡힌 세상

while (True):
    stack = []
    word = input()

    if (word == "."):
        break

    for s in word:
        if (s == "(") or (s == "["):
            stack.append(s)

        elif (s == ")"):
            if (stack) and (stack[-1] == "("):
                stack.pop()
            else:
                stack.append(s)
                break

        elif (s == "]"):
            if (stack) and (stack[-1] == "["):
                stack.pop()
            else:
                stack.append(s)
                break

    print("no" if stack else "yes")