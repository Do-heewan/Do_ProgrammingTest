a, b = input().split()

num1 = int(a[::-1])
num2 = int(b[::-1])

if (num1 > num2):
    print(num1)
else:
    print(num2)