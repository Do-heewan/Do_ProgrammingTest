def sum(a, b):
    return a + b

def min(a, b):
    return a - b

a, b = map(int, input().split())

mul = sum(a, b) * min(a, b)
print(mul)