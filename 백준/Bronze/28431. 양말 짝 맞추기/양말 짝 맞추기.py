li = []
for _ in range(5):
    num = int(input())
    if (num in li):
        li.remove(num)
    else:
        li.append(num)

print(*li)