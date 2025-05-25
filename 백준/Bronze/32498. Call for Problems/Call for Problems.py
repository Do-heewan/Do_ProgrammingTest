N = int(input())

count = 0
for _ in range(N):
    num = int(input())
    
    if (num % 2 != 0):
        count += 1

print(count)