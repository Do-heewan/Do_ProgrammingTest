# 2164 카드2

from collections import deque

N = int(input())

queue = deque()
for i in range(1, N+1):
    queue.append(i)

while len(queue) > 1:
    # 1. 제일 첫번째 카드를 버린다.
    queue.popleft()

    # 2. 두 번째 카드를 맨 뒤로 보낸다.
    c = queue.popleft()
    queue.append(c)

print(*queue)