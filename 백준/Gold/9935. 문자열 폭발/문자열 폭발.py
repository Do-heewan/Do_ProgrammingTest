# 9935 문자열 폭발

word = input()
exp = list(input())

# while word:
#     if exp in word:
#         word = word.replace(exp, '')
    
#     else:
#         break

# print(word) if word else print("FRULA")

stack = []

for w in word:
    stack.append(w)

    if exp[:] == stack[-len(exp):]:
        for _ in range(len(exp)):
            stack.pop()

if stack:
    for ix in stack:
        print(ix, end='')
else:
    print("FRULA")