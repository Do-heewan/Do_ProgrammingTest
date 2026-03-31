# 14003 가장 긴 증가하는 부분 수열 5

import bisect

N = int(input())
lst = list(map(int, input().split()))

seq = []
route = [0] * N

for i in range(N):
    x = lst[i]
    idx = bisect.bisect_left(seq, x)

    if idx == len(seq):
        seq.append(x)
    else:
        seq[idx] = x

    route[i] = idx

print(len(seq))

result = []
curr = len(seq)-1

for i in range(N-1, -1, -1):
    if route[i] == curr:
        result.append(lst[i])
        curr -= 1

print(*result[::-1])