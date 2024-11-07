n = int(input())

count = 0
for i in range(n):
    d, num = input().split('-')
    if (int(num) <= 90):
        count += 1

print(count)