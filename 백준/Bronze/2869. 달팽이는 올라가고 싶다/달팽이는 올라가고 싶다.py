a, b, v = map(int, input().split())

if ((v - b) % (a - b) == 0):
    result = (v - b) // (a - b)
elif ((v - b) % (a - b) != 0):
    result = (v - b) // (a - b) + 1

print(result)