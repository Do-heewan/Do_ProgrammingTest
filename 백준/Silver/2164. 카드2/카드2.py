# 2164 카드2

from collections import deque

N = int(input())

Q = deque()
for i in range(1, N+1):
    Q.append(i)

while (len(Q) > 1):
    Q.popleft()
    Q.append(Q.popleft())

print(*Q)