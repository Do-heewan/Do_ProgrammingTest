a, b = map(int, input().split())

if a not in [0, 2, 5] and b not in [0, 2, 5]:
    print("=")
elif a not in [0, 2, 5]:
    print("<")
elif b not in [0, 2, 5]:
    print(">")
else:
    if a == b:
        print("=")
        
    elif a == 0:
        if b == 5:
            print("<")
        else:
            print(">")
    elif a == 2:
        if b == 5:
            print(">")
        else:
            print("<")
    else:
        if b == 0:
            print(">")
        else:
            print("<")