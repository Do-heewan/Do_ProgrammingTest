num = list(map(int, input().split()))
num = [x ** 2 for x in num]
a = sum(num) % 10
print(a)