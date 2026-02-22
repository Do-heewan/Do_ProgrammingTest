# 1213 팰린드롬 만들기

word = input().strip()

word_dict = {}
for w in word:
  word_dict[w] = word_dict.get(w, 0) + 1

odd_count = 0
sorted_keys = sorted(word_dict.keys())

prefix = ''
mid = ''
for k in sorted_keys:
  v = word_dict[k]
  if v % 2 == 1:
    mid += k
    odd_count += 1
  prefix += k * (v // 2)

postfix = prefix[::-1]

if odd_count > 1:
  print('I\'m Sorry Hansoo')
else:
  print(prefix + mid + postfix)
