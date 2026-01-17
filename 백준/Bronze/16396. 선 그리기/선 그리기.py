N = int(input())

lines = [0] * (10001)
for _ in range(N):
    a, b = map(int, input().split())
    for i in range(a, b):
        lines[i] = 1

print(sum(lines))