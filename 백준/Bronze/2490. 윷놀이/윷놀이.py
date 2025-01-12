# 2490 윷놀이

for _ in range(3):
    s = list(map(int, input().split()))
    if (sum(s) == 3):
        print("A")
    elif (sum(s) == 2):
        print("B")
    elif (sum(s) == 1):
        print("C")
    elif (sum(s) == 0):
        print("D")
    else:
        print("E")