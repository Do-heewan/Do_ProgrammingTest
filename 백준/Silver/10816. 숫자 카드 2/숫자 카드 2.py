# 10816 숫자 카드 2

from collections import Counter

N = int(input())
nums = list(map(int, input().split()))

M = int(input())
target = list(map(int, input().split()))

num_set = Counter(nums)

for t in target:
    if t in num_set.keys():
        print(num_set[t])
    else:
        print(0)