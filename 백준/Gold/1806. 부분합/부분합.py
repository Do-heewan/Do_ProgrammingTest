# 1806 부분합

N, S = map(int, input().split())
lst = list(map(int, input().split()))

start = 0
answer = 100_000

temp = 0
for end in range(N):
    temp += lst[end]

    while temp >= S:
        answer = min(answer, (end-start+1))
        temp -= lst[start]
        start += 1

print(answer if answer != 100_000 else 0)