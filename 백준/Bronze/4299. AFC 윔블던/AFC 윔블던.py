# 4299 AFC 윔블던

sum, min = map(int, input().split())

A = (sum + min)
B = (sum - min)

if (A % 2 != 0) or (B % 2 != 0) or (B < 0):
    print(-1)
else:
    A //= 2
    B //= 2

    if (A < B):
        A, B = B, A
    print(A, B)