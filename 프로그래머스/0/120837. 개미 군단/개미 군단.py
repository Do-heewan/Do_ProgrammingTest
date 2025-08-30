def solution(hp):
    cnt = 0
    while (hp > 0):
        if (hp >= 5):
            hp -= 5
            cnt += 1
        elif (hp >= 3):
            hp -= 3
            cnt += 1
        else:
            hp -= 1
            cnt += 1
    return cnt