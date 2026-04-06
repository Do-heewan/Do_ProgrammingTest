# 14003 가장 긴 증가하는 부분 수열 5

import sys
input = sys.stdin.readline

def binary_search(left, right, target, arr):
    while left < right:
        mid = (left+right) // 2

        if arr[mid] < target:
            left = mid+1
        else:
            right = mid
    
    return left

N = int(input())
lst = list(map(int, input().split()))

dp = []
route = [0] * N
for i in range(N):
    curr = lst[i]
    idx = binary_search(0, len(dp), curr, dp)

    if len(dp) == idx:
        dp.append(curr)
        
    else:
        dp[idx] = curr

    route[i] = idx

print(len(dp))

start = len(dp)-1
result = []
for i in range(N-1, -1, -1):
    if route[i] == start:
        result.append(lst[i])
        start -= 1

result.reverse()
print(*result)