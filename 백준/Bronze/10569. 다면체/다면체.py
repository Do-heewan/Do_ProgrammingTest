T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(abs(a-b)+2)