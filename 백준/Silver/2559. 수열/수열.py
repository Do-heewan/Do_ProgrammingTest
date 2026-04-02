# 2559 수열

N, K = map(int, input().split())
lst = list(map(int, input().split()))

visited = [0] * 100001

start = 0
answer = -100_000

tmp = 0
for end in range(N):
    tmp += lst[end]

    if (end-start+1) == K:
        answer = max(answer, tmp)
        tmp -= lst[start]
        start += 1

print(answer)