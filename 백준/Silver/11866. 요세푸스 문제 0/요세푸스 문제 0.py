# 요세푸스 문제 0

from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

Q = deque()
for i in range(1, N+1):
    Q.append(i)

result = []
while Q:
    for _ in range(K-1):
        c = Q.popleft()
        Q.append(c)

    result.append(Q.popleft())

print("<", end = '')
for i in range(len(result)-1):
    print(result[i], end = ", ")
print(result[-1], end = '')
print(">")