#  4375 1

while True:
    try:
        num = int(input())
        one = 1
        cnt = 1
        while one % num != 0:
            one = one * 10 + 1
            cnt += 1
            
        print(cnt)

    except:
        break