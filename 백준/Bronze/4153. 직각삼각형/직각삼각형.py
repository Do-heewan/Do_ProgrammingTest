while (True):
    A, B, C = map(int, input().split())
    if (A == 0) and (B == 0) and (C == 0):
        break
    elif (A > B) and (A > C):
        if (A * A == B * B + C * C):
            print("right")
        else:
            print("wrong")
    elif (B > C):
        if (B * B == A * A + C * C):
            print("right")
        else:
            print("wrong")
    else:
        if (C * C == A * A + B * B):
            print("right")
        else:
            print("wrong")