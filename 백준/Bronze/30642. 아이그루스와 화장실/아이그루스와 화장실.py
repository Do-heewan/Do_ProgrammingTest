K = int(input())
name = input()
N = int(input())

if (name == "annyong"):
    if (N % 2 == 0):
        print(N-1)
    else:
        print(N)
        
elif (name == "induck"):
    if (N % 2 == 0):
        print(N)
    elif (N > 1):
        print(N-1)
    else:
        print(N+1)