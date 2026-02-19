# 1041 주사위

N = int(input())
A, B, C, D, E, F = map(int, input().split())
dice = [A, B, C, D, E, F]

if N == 1:
    print(sum(dice) - max(dice))

else:
    a = min(A, F)
    b = min(B, E)
    c = min(C, D)

    one = min(a, b, c)
    two = min(a+b, b+c, c+a)
    three = a+b+c

    corner = 4
    edge = (N-2)*4 + (N-1)*4
    center = (N-2)**2 * 5 + (N-2)*4

    print(one * center + two * edge + three * corner)