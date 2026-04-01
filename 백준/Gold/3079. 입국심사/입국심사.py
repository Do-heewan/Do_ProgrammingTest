# 3079 입국심사

def check(mid):
    cnt = 0

    for t in times:
        cnt += mid // t

    return cnt >= M

def binary_search(start, end):
    answer = 0

    while start <= end:
        mid = (start+end) // 2

        if check(mid):
            end = mid-1
            answer = mid

        else:
            start = mid+1
    
    return answer

N, M = map(int, input().split())
times = [int(input()) for _ in range(N)]

left, right = 1, M * max(times)

print(binary_search(left, right))