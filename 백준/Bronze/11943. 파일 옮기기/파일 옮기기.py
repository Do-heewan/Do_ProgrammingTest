a = list(map(int, input().split()))
b = list(map(int, input().split()))

target = min(a[0] + b[1], a[1] + b[0])
print(target)