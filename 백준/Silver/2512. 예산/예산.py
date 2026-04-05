# 2512 예산

def check(mid):
    total_money = 0
    for m in money:
        if m < mid:
            total_money += m
        else:
            total_money += mid

    if total_money <= limit:
        return True
    else:
        return False

def binary_search(start, end):
    answer = 0

    while start <= end:
        mid = (start+end) // 2

        if check(mid):
            answer = mid
            start = mid+1
        else:
            end = mid-1

    return answer

N = int(input())
money = list(map(int, input().split()))
limit = int(input())

if sum(money) <= limit:
    print(max(money))

else:
    start = 0
    end = max(money)

    print(binary_search(start, end))