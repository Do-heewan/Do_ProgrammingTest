# 1920 수 찾기

def binary_search(start, end, target):
    while start < end:
        mid = (start+end) // 2

        if lst[mid] < target:
            start = mid+1
        else:
            end = mid

    return lst[start] == target

N = int(input())
lst = list(map(int, input().split()))
lst.sort()

M = int(input())
target = list(map(int, input().split()))

for t in target:
    print(1 if binary_search(0, N-1, t) else 0)