# 14470 전자레인지

A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

result = 0
if (A < 0):
    result += C * -A
    result += D
    result += E * B
else:
    result += E * (B - A)

print(result)