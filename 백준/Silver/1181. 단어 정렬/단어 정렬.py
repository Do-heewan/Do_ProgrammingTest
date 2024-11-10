n = int(input())
word = []

for i in range(n):
    word.append(input())

set_word = set(word)
word = list(set_word)
word.sort()	# 괄호 안에 아무 값도 넣지 않으면 알파벳 순서대로 정렬을 해 준다.
word.sort(key = len)	# 문자열 길이 순으로 정렬.

for i in word:
    print(i)