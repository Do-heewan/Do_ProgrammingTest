# 1654 랜선 자르기

def check(arr, mid):
    cnt = 0
    for a in arr:
        cnt += a // mid

    if cnt >= K:
        return True
    else:
        return False

def binary_search(arr, start, end):
    result = 0

    while start <= end:
        mid = (start+end) // 2

        if mid == 0:
            return 0

        if check(arr, mid):
            result = mid
            start = mid+1
        else:
            end = mid-1

    return result
        

N, K = map(int, input().split())
lan = [int(input()) for _ in range(N)]

start, end = 1, max(lan)

print(binary_search(lan, start, end))