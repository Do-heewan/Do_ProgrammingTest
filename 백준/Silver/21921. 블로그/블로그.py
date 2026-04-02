# 21921 블로그

N, X = map(int, input().split())
lst = list(map(int, input().split()))

start = 0
answer = 0

tmp = 0
cnt = 0
for end in range(N):
    tmp += lst[end]

    if (end-start+1) == X:
        if tmp > answer:
            answer = tmp
            cnt = 1
        elif tmp == answer:
            cnt += 1

        tmp -= lst[start]
        start += 1

if answer:
    print(answer)
    print(cnt)
else:
    print("SAD")