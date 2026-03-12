num = int(input())

sum = 0
square = 0
volume = 0

for i in range(num):
    sum += (i + 1)
    volume += (i + 1) ** 3

square = sum ** 2

print(sum)
print(square)
print(volume)