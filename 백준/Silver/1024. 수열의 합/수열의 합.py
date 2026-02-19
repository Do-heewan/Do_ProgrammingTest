# 1024 수열의 합

N, L = map(int, input().split())

for i in range(L, 101):
    ix = N - i*(i+1)//2

    if ix % i == 0:
        x = ix // i
        if x+1 >= 0:
            print(*(i for i in range(x+1, x+i+1)))
            break

else:
    print(-1)