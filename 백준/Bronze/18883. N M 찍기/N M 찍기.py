n, m = map(int, input().split())
k = n * m

for i in range(1, k + 1):
    if i % m == 0:
        print(i)
    else:
        print(i, end=" ")