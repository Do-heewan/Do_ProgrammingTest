# 12015 가장 긴 증가하는 부분 수열 2

def binary_search(dp, target):
    start, end = 0, len(dp)

    while start < end:
        mid = (start+end) // 2
        
        if dp[mid] < target:
            start = mid+1
        else:
            end = mid

    return start

N = int(input())
lst = list(map(int, input().split()))

dp = []

for x in lst:
    idx = binary_search(dp, x)

    if idx == len(dp):
        dp.append(x)
    else:
        dp[idx] = x

print(len(dp))