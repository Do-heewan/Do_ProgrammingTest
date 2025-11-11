# 1002 터렛

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    if x1 == x2 and y1 == y2 :
        if r1 == r2 :
            print(-1)
        else:
            print(0)
        continue
    if (x1 - x2) ** 2 + (y1 - y2) ** 2 in ((r1 - r2)**2, (r1 + r2)**2) :
        print(1)
    elif (r1 - r2)**2 < (x1 - x2) ** 2 + (y1 - y2) ** 2 < (r1 + r2)**2 :
        print(2)
    else:
        print(0)
