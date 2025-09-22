T = int(input())

for _ in range(T):
    C = int(input())

    for ix in [25, 10, 5, 1]:
        print(C // ix, end = ' ')
        C %= ix
    print()