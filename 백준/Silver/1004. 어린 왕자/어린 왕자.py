# 1004 어린 왕자

def checkIn(targetX, targetY, x, y, r):
    if (x-targetX) ** 2 + (y-targetY) ** 2 <= r ** 2:
        return True
    return False

T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    N = int(input())

    cnt = 0
    for _ in range(N):
        x, y, r = map(int, input().split())

        if (checkIn(x1, y1, x, y, r) and not checkIn(x2, y2, x, y, r)) or (not checkIn(x1, y1, x, y, r) and checkIn(x2, y2, x, y, r)):
            cnt += 1

    print(cnt)