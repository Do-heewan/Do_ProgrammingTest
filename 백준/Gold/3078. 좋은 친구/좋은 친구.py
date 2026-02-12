# 3078 좋은 친구

import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

window = deque()
len_count = [0] * 21

ans = 0
for _ in range(N):
    curr = input().strip()

    ans += len_count[len(curr)]

    window.append(len(curr))
    len_count[len(curr)] += 1

    if len(window) > K:
        old_len = window.popleft()
        len_count[old_len] -= 1

print(ans)