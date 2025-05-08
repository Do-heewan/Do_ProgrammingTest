# 1541 잃어버린 괄호

seq = input().split("-")

num = []

for ix in seq:
    sum = 0
    tmp = ix.split("+")
    for i in tmp:
        sum += int(i)
    
    num.append(sum)
n = num[0]

for i in range(1, len(num)):
    n -= num[i]

print(n)