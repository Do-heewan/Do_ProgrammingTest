lst = list(map(int, input().split()))
x, y, r = map(int, input().split())

res = []
for i in range(len(lst)):
    if lst[i] == x:
        res.append(i+1)

print(*res) if res else print(0)