# 1394 암호

word = list(input())
cipher = input()

word_dict = {}
for i in range(1, len(word)+1):
    word_dict[word[i-1]] = i

answer = 0
for c in cipher:
    answer = (answer * len(word) + word_dict[c]) % 900528

print(answer)