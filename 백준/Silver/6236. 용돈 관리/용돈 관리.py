# 6236 용돈 관리

def check(mid):
    cnt = 1
    curr_money = mid
    
    for m in money:
        if curr_money < m:
            curr_money = mid
            cnt += 1
        curr_money -= m

    if cnt <= M:
        return True
    else:
        return False

def binary_search(start, end):
    answer = 0

    while start <= end:
        mid = (start+end) // 2

        if check(mid):
            answer = mid
            end = mid-1
        else:
            start = mid+1

    return answer

N, M = map(int, input().split())
money = [int(input()) for _ in range(N)]

start, end = max(money), sum(money)

print(binary_search(start ,end))