# 5585 거스름돈

money = 1000 - int(input())
coin = [500, 100, 50, 10, 5, 1]

count = 0
for c in coin:
    if money >= c:
        count += (money // c)
    money %= c

print(count)