num = int(input())
size = list(map(int, input().split()))
t, p = list(map(int, input().split()))

count = 0
for i in range(len(size)):
    if (size[i] % t == 0):
        count += size[i] // t
    else:
        count += size[i] // t + 1

pen = [num // p, num % p]

print(count)
print(pen[0], pen[1])