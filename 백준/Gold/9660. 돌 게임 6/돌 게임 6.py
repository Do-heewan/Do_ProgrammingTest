# 9660 돌 게임 6

N = int(input())

if N == 2:
    print("SK")
elif N % 7 == 0 or N % 7 == 2:
    print("CY")
else:
    print("SK")