# 5341 Pyramids

while (1):
    num = 0
    N = int(input())

    for i in range(N, 0, -1):
        num += i
    
    if (N == 0):
        break

    print(num)