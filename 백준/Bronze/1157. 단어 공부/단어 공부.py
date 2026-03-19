# 1157 단어공부

from collections import Counter

word = input().lower()
count = Counter(word)

res = ''
cnt = 0
max_val = max(count.values())

for k, v in count.items():
    if v == max_val:
        cnt += 1
        res = k

print(res.upper() if cnt == 1 else "?")