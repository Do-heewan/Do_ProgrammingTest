# 4084 Viva la Diferencia

while True:
    lst = list(map(int, input().split()))
    
    if sum(lst) == 0:
        break

    cnt = 0
    while True:
        if lst[0] == lst[1] and lst[1] == lst[2] and lst[2] == lst[3]:
            print(cnt)
            break

        temp = lst.copy()
        lst[0] = abs(temp[0] - temp[1])
        lst[1] = abs(temp[1] - temp[2])
        lst[2] = abs(temp[2] - temp[3])
        lst[3] = abs(temp[3] - temp[0])
        cnt += 1