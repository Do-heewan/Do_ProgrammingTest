word2 = []
test = int(input())

for i in range(test):
    num, word = input().split()
    num = int(num)
    for j in range(len(word)):
        print(word[j] * num, end='')
    print("")