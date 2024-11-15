a = []
count = 0

for i in range(10):
    num = int(input())
    a.append(num % 42)

new_a = list(set(a))

print(len(new_a))