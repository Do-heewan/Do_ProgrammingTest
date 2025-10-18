g = list(map(int, input().split()))
e = list(map(int, input().split()))

if sum(g) == sum(e):
    print("Tie")
elif sum(g) > sum(e):
    print("Gunnar")
else:
    print("Emma")