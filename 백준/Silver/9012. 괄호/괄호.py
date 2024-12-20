# 9012 괄호

n = int(input())


for i in range(n):
    word = list(input())
    count = 0

    for j in range(len(word)):
        if (word[j] == ('(')):
            count += 1
        else:
            count -= 1

        if (count < 0):
            print("NO")
            break

    if (count > 0):
        print("NO")
    elif (count == 0):
        print("YES")
