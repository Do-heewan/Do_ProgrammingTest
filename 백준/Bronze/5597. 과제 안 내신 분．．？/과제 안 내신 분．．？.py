ran = 29

a = list(range(1, 31))

for i in range(28):
    num = int(input())
    for j in range(ran):
        if (a[j] == num):
            a.remove(num)
            ran = ran - 1

for i in range(2):
    print(a[i])