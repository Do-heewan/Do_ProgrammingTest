# 25192 인사성 밝은 곰곰이

import sys
input = sys.stdin.readline

N = int(input().rstrip())

chat = {}
cnt = 0
for _ in range(N):
    word = input().rstrip()

    if word == "ENTER":
        cnt += sum(chat.values())
        chat = {}

    else:
        chat[word] = chat.get(word, 1)

cnt += sum(chat.values())
print(cnt)