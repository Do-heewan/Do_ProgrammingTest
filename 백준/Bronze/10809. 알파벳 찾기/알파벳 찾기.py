word = input()

alpList = [-1] * 26
for i in range(len(word)):
    index = ord(word[i]) - 97
    if (alpList[index] == -1):
        alpList[index] = i

print(*alpList)