# 2110 공유기 설치

N, M = map(int, input().split())
port = [int(input()) for _ in range(N)]
port.sort()

left, right = 1, port[-1] - port[0]

answer = 0
while left <= right:
    mid = (left+right) // 2

    curr = port[0]
    cnt = 1

    for i in range(1, N):
        if port[i] >= curr + mid:
            curr = port[i]
            cnt += 1

    if cnt >= M:
        left = mid+1
        answer = mid
    else:
        right = mid-1

print(answer)