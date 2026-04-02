# 2003 수들의 합 2

N, M = map(int, input().split())
lst = list(map(int, input().split()))

start = 0
answer = 0

tmp = 0
for end in range(N):
    tmp += lst[end]

    while tmp >= M:
        if tmp == M:
            answer += 1
            
        tmp -= lst[start]
        start += 1

print(answer)