# 2230 수 고르기

N, M = map(int, input().split())
lst = [int(input()) for _ in range(N)]
lst.sort()

start = 0
answer = 2_000_000_000

tmp = 0
for end in range(N):

    while start <= end and lst[end] - lst[start] >= M:
        answer = min(answer, lst[end] - lst[start])
        start += 1

print(answer)