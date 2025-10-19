# 1476 날짜 계산

E, S, M = map(int, input().split())

cnt = 0
while True:
    if E == 0 and S == 0 and M == 0:
        break

    if E == 0:
        E = 15
    if S == 0:
        S = 28
    if M == 0:
        M = 19

    E -= 1
    S -= 1
    M -= 1

    cnt += 1

print(cnt)