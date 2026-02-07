# 1174 줄어드는 수

from collections import deque

def bfs():
    Q = deque()
    result = []

    for i in range(10):
        Q.append(i)
    
    while Q:
        num = Q.popleft()
        result.append(num)

        last_digit = num % 10

        for next_digit in range(last_digit):
            next_num = num * 10 + next_digit
            Q.append(next_num)

    return sorted(result)

N = int(input())
nums = bfs()

print(nums[N-1] if N-1 < len(nums) else -1)