num = int(input())
numList = list(map(int, input().split()))
value = int(input())

count = 0

for i in range(num):
    if (numList[i] == value):
        count = count + 1

print(count)