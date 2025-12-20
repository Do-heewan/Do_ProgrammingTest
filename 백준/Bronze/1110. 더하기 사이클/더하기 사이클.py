a = int(input())
b = a

cnt = 0
while True:
    a = (a%10)*10 + ((a//10) + (a%10))%10
    cnt += 1

    if a == b:
        break

print(cnt)