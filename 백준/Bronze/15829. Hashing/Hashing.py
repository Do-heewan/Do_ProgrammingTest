num = int(input())
word = input()
sum = 0

for i in range(num):
    word_num = ord(word[i]) - 96
    sum = sum + (31 ** i * word_num)

print(sum % 1234567891)