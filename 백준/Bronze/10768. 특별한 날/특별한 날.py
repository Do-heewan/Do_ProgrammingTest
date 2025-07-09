M = int(input())
D = int(input())

if (M == 2) and (D == 18):
    print("Special")
elif (M > 2) or ((M == 2) and (D > 18)):
    print("After")
else:
    print("Before")
