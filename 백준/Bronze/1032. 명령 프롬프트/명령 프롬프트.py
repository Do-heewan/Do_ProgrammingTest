# 1032 명령프롬프트

N = int(input())

curr = []
for _ in range(N):
    word = input()

    if not curr:
        curr = list(word)
        continue

    for i in range(len(curr)):
        if curr[i] != word[i]:
            curr[i] = "?"

print(*curr, sep="")