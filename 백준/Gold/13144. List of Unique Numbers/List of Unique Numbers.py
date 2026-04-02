# 13144 List of Unique Numbers

N = int(input())
lst = list(map(int, input().split()))

visited = [0] * 100001

start = 0
answer = 0

for end in range(N):
    while visited[lst[end]] == 1:
        visited[lst[start]] = 0
        start += 1

    visited[lst[end]] = 1
    answer += (end-start + 1)

print(answer)