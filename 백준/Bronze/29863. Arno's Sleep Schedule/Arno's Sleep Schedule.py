A = int(input())
B = int(input())

n_A = (24 - A) if (A >= 20) else A

print(n_A + B if (A >= 20) else B - A)