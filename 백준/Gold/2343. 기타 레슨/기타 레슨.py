# 2343 기타 레슨

def check(mid):
    cnt = 1
    volume = 0

    for b in blue_ray:
        if volume + b > mid:
            cnt += 1
            volume = 0
        volume += b

    return cnt <= M

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
blue_ray = list(map(int, input().split()))

start, end = max(blue_ray), sum(blue_ray)

print(binary_search(start, end))