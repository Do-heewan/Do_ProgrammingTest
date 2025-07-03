# 2444 별 찍기 - 7

N = int(input())

star = [' ' for _ in range(N)]
star[N-1] = "*"

for ix in star:
    print(ix, end='')
print()

for i in range(1, N):
    star[N-i-1] = "*"
    star.append("*")
    
    for ix in star:
        print(ix, end="")
    print()

for i in range(N, 0, -1):
    star[N-i] = " "
    star.pop()

    for ix in star:
        print(ix, end="")
    print()