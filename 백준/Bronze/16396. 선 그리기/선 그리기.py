# 16396 선 그리기

N = int(input())
line = [0] * 10001
for _ in range(N):
    a, b = map(int, input().split())
    for i in range(a, b):
        line[i] = 1

print(sum(line))