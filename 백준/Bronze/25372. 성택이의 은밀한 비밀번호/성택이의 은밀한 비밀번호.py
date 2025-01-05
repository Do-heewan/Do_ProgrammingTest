# 25372 성택이의 은밀한 비밀번호

T = int(input())

for _ in range(T):
    passwd = input()

    if (len(passwd) >= 6) and (len(passwd) <= 9):
        print("yes")
    else:
        print("no")