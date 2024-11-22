test = int(input())

for i in range(test):
    O_X = input()
    result = 0
    score = 0
    for j in range(len(O_X)):
        if (O_X[j] == "O"):
            score += 1
            result += score
        elif (O_X[j] == "X"):
            score = 0
    print(result)