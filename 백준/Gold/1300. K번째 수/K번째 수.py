# 1300 k번째 수

def binary_search(start, end, target):
    answer = 0

    while start <= end:
        mid = (start+end) // 2

        cnt = 0
        for i in range(1, N+1):
            cnt += min(mid // i, N)

        if cnt < target: 
            start = mid+1
        else: 
            answer = mid
            end = mid - 1

    return answer

N = int(input())
k = int(input())

print(binary_search(0, k, k))