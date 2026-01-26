A, T = map(int, input().split())
P = 10 + 2 * (25 - A + T)
print(P if P > 0 else 0)