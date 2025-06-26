# 14626 ISBN

ISBN = input()

check_sign = int(ISBN[-1])
weight = [1, 3] * 6
result = 0

for i in range(len(ISBN) - 1):
    if (ISBN[i] == "*"):
        target = weight[i]
        continue

    result += int(ISBN[i]) * weight[i]

for i in range(1, 10):
    if ((result + check_sign + i * target) % 10 == 0):
        print(i)
        break
else:
    print(0)