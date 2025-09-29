# 11034 캥거루 세마리2

while True:
    try:
        k = list(map(int, input().split()))
        k.sort()

        a = k[2] - k[1]
        b = k[1] - k[0]

        print(b-1 if a < b else a-1)

    except EOFError:
        break