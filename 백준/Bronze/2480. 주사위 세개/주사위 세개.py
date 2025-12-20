a, b, c = map(int, input().split())

answer = 0
if a == b == c:
    answer = 10000 + 1000 * a

elif a == b:
    answer = 1000 + 100 * a

elif b == c:
    answer = 1000 + 100 * b

elif c == a:
        answer = 1000 + 100 * c

else:
    answer = max(a, b, c) * 100

print(answer)