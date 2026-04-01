# 10815 숫자 카드

def binary_search(left, right, target):
    while left < right:
        mid = (left+right) // 2

        if lst[mid] < target:
            left = mid+1
        else:
            right = mid

    if left < N and lst[left] == target:
        return 1
    else:
        return 0

N = int(input())
lst = list(map(int, input().split()))
lst.sort()

M = int(input())
target = list(map(int, input().split()))

for t in target:
    print(binary_search(0, N-1, t), end=' ')